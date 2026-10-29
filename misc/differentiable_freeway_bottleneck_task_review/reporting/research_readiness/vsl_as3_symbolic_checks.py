"""AS3 exact symbolic/rational checks; no simulator, rollout or numerical AD.

Checks new fixed-E asymmetric preparation and full reference costs, then
independent-lane arrival/root/history identities. These support algebra,
not a machine proof of comparison, regularity, physical validity or useful
implemented gradients. No numerical trajectory or optimizer is run.
"""

from pathlib import Path
import json
import sympy as sp


def main() -> None:
    identities: dict[str, bool] = {}
    static: dict[str, bool] = {}

    def identity(name: str, expression: sp.Expr) -> None:
        identities[name] = bool(sp.simplify(expression) == 0)

    q=sp.Rational
    v,u,k,h,ell,R,c0=sp.symbols('v u k h ell R c0',positive=True)
    delta=6*k*u/(2*u+v)-q(19,20)*k
    high=q(5,6)*(q(3,5)*k+delta)**2/(4*delta)
    low=k/2; vc=q(58,31)*u
    identity('receiving_threshold_critical_density',6*k*u/(2*u+vc)-q(31,20)*k)
    identity('high_front_matches_donor_at_threshold',high.subs(v,vc)-low)
    identity('high_front_first_derivative_matches',sp.diff(high,v).subs(v,vc))
    identity('new_asymmetric_high_front',high.subs(v,2*u)-q(529,1056)*k)
    identity('new_asymmetric_high_front_derivative',sp.diff(high,v).subs(v,2*u)-q(115,7744)*k/u)
    identity('new_asymmetric_low_front_derivative',sp.diff(low,v))
    identity('high_forced_mass_derivative',(h*sp.diff(high,v)/6).subs(v,2*u)-q(115,46464)*h*k/u)

    B,r,Ttravel,s=sp.symbols('B r Ttravel s',positive=True)
    duration=ell/v; D=ell*r-R*duration
    forced=h*B*(1-sp.exp(-ell/h)); moment=h*B*ell-h*forced
    queue=((v*r-R)*s+(c0-1)*h*B*(1-sp.exp(-v*s/h)))/c0
    identity('reference_queue_starts_empty',queue.subs(s,0))
    identity('reference_queue_balance',sp.diff(queue,s)-((v*r-R)+(c0-1)*v*B*sp.exp(-v*s/h))/c0)
    identity('reference_rear_queue',queue.subs(s,duration)-(D+(c0-1)*forced)/c0)
    pulsearea=sp.integrate(queue,(s,0,duration))
    identity('complete_pulse_area',pulsearea-D*duration/(2*c0)-(1-1/c0)*moment/v)
    J=Ttravel/v+D*duration/(2*c0)+(1-1/c0)*moment/v+(D+(c0-1)*forced)**2/(2*c0*R)
    I0=(Ttravel+moment)/v+(D-forced)*forced/R
    I1=D*duration/2-moment/v+(D-forced)**2/(2*R)
    identity('new_complete_objective_expansion',J-c0*forced**2/(2*R)-I0-I1/c0)
    W=ell*r+(c0-1)*forced
    coef=Ttravel+(1-1/c0)*(moment-ell*forced)-ell*ell*r/(2*c0)
    identity('donor_only_inverse_speed_objective',J-W**2/(2*c0*R)-coef/v)
    identity('positive_low_coefficient_remainder',coef-(Ttravel-ell*ell*r)-((1-1/c0)*(moment+ell*(ell*r-forced))+ell*ell*r/(2*c0)))
    identity('low_complete_derivative',sp.diff(J,v)+coef/v**2)

    a,p,beta=sp.symbols('a p beta',positive=True)
    mu0=(R-a)/c0; muminus=(R-p-a)/(c0+beta)
    identity('selected_service_bracket_difference',mu0-muminus-(beta*(R-a)+c0*p)/(c0*(c0+beta)))
    identity('selected_service_uniform_remainder',p/c0+R*beta/c0**2-(mu0-muminus)-beta*(c0*p+R*beta+c0*a)/(c0**2*(c0+beta)))
    H,eps=sp.symbols('H eps',positive=True)
    identity('uniform_objective_area_bound',sp.integrate(s*eps,(s,0,H))-H**2*eps/2)

    t,L,Lp,b,b0=sp.symbols('t L Lp b b0',positive=True)
    x,z=sp.symbols('x z',real=True);density=sp.Function('e')
    PE=sp.Integral(density(Lp-x,v),(x,L-v*t,ell))
    PEv=sp.Integral(sp.diff(density(Lp-x,v),v),(x,L-v*t,ell))+t*density(Lp-L+v*t,v)
    identity('independent_initial_E_moving_count',sp.diff(PE,v)-PEv)
    PA=r*(ell-L+v*t)-PE; PB=b0*(ell-L+v*t)
    identity('independent_A_moving_count',sp.diff(PA,v)-(r*t-sp.diff(PE,v)))
    identity('independent_B_moving_count',sp.diff(PB,v)-b0*t)
    PEend=sp.Integral(density(Lp-x,v),(x,0,ell))
    identity('final_total_mass_derivative',sp.diff(PEend+(ell*r-PEend)+ell*b0,v))
    identity('three_lane_travel_numerator',sp.integrate((r+b0)*(L-x),(x,0,ell))-ell*(r+b0)*(L-ell/2))

    K,w,g,chi,ua=sp.symbols('K w g chi ua',positive=True)
    U=lambda flow:w*flow/(K-flow)
    root=g*(c0+chi*a*(ua-U(g)))
    Hg=c0+chi*a*(ua-U(g)-g*sp.diff(U(g),g))
    identity('fixed_coefficient_root_flow_partial',sp.diff(root,g)-Hg)
    identity('fixed_coefficient_root_A_partial',sp.diff(root,a)-chi*g*(ua-U(g)))
    identity('fixed_coefficient_root_mark_partial',sp.diff(root,ua)-chi*a*g)
    oldrate,Zt,Zo,Do=sp.symbols('oldrate Zt Zo Do',nonzero=True)
    identity('history_retirement_old_rate_cancels',-Do*oldrate*(Zt-Zo)/oldrate+Do*(Zt-Zo))
    aa,bb,cc,cutoff,tau=[sp.Function(name)(v) for name in ['aa','bb','cc','cutoff','tau']]
    left,right=aa*s+bb,cc*s*s
    integral=sp.integrate(left,(s,cutoff,tau))+sp.integrate(right,(s,tau,t))
    leibniz=(sp.integrate(sp.diff(left,v),(s,cutoff,tau))+sp.integrate(sp.diff(right,v),(s,tau,t))
             +(left.subs(s,tau)-right.subs(s,tau))*sp.diff(tau,v)-left.subs(s,cutoff)*sp.diff(cutoff,v))
    identity('history_moving_event_and_cutoff_terms',sp.diff(integral,v)-leibniz)
    fm,fp,end=sp.symbols('Fminus Fplus end',nonzero=True)
    level=sp.Function('level')(v); event=level/fm
    endpoint=level+fp*(end-event)
    identity('identity_reset_event_time_correction',sp.diff(endpoint,v)-(fm-fp)*sp.diff(event,v))
    qa,qb=sp.Function('qa')(v),sp.Function('qb')(v)
    curve=(t-qa)*(qb-t)
    identity('zero_queue_endpoint_area_values',sp.diff(sp.integrate(curve,(t,qa,qb)),v)-sp.integrate(sp.diff(curve,v),(t,qa,qb)))

    neg=q(132,2645)
    checks={
        'same_E_and_main_total':q(3,5)+q(1,5)+q(7,20)==q(3,5)+q(7,20)+q(1,5)==q(23,20),
        'different_adjacent_load_at_fixed_E':q(1,5)!=q(7,20),
        'ordinary_pair_margin':q(39,20)-2*q(19,20)==q(1,20)>0,
        'far_margin':1-2*q(7,20)==q(3,10)>0,
        'finite_storage_fraction':q(23,20)/3==q(23,60)<1,
        'same_loading_subfamily':1<q(6,5)<q(4,3),
        'low_always_donor':q(3,2)-q(4,5)==q(7,10)>q(3,5),
        'high_advice_switch_inside_interval':1<q(58,31)<2,
        'high_switch_before_first_exposure':q(23,22)**2<q(6,5),
        'positive_preparation_response':q(115,7744)>0,
        'latest_handoff_density_bound':q(3,5)*q(5,6)**2==q(5,12),
        'new_sustained_queue_threshold':q(4,5)+(q(94,25)-1)*q(5,12)==q(39,20),
        'positive_common_action_interval':0<neg<q(1,10),
        'high_front_free_threshold_exact':q(19,10)+q(529,528)*neg==q(39,20),
        'low_front_free_at_threshold':q(8,5)+neg<q(39,20),
        'travel_numerator_exceeds_low_pair_term':q(23,8)>q(4,5),
        'travel_numerator_exceeds_high_pair_term':q(23,8)>q(19,20),
        'mismatch_root_range_not_empty':q(94,25)>2,
    }
    static.update({name:bool(value) for name,value in checks.items()})
    failures=[name for name,okay in {**identities,**static}.items() if not okay]
    result={
        'date':'2026-10-19','passed':not failures,
        'scope':'Exact asymmetric preparation/full-cost/sensitivity identities and rational inequalities only; no traffic/AD/numerical-gradient experiment',
        'sympy_version':sp.__version__,
        'symbolic_identity_count':len(identities),'static_check_count':len(static),
        'symbolic_identities':identities,'static_checks':static,'failures':failures,
        'limits':'These checks support algebra, not independent certification of the comparison theorem, regularity, physical ranges, actual infinitesimal gradient signs or optimizer usefulness.',
    }
    Path(__file__).with_name('vsl_as3_symbolic_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['passed','sympy_version','symbolic_identity_count','static_check_count','failures']},indent=2))
    if failures:raise SystemExit(1)


if __name__=='__main__':
    main()
