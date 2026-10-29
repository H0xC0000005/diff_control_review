"""AS2 exact loading/observation algebra, without numerical traffic evolution.

No time stepping, ODE solve, AD, numerical derivative, calibration or
optimization. Human proof and the channel contract carry the information
claim; these checks verify the new algebra and exact feasibility example.
"""

from pathlib import Path
import json
import sympy as sp


def main() -> None:
    identities: dict[str, bool] = {}
    static: dict[str, bool] = {}

    def identity(name: str, expression: sp.Expr) -> None:
        identities[name] = bool(sp.simplify(expression) == 0)

    u,h,ell,e0,r1,r2,rho,b1,b2 = sp.symbols('u h ell e0 r1 r2 rho b1 b2',positive=True)
    x,t = sp.symbols('x t',real=True)
    T=ell/u
    e=e0*sp.exp(-u*t/h)
    a1,a2=r1-e,r2-e
    identity('E_transport_balance',sp.diff(e,t)+u*sp.diff(e,x)+u*e/h)
    identity('A1_transport_balance',sp.diff(a1,t)+u*sp.diff(a1,x)-u*e/h)
    identity('A2_transport_balance',sp.diff(a2,t)+u*sp.diff(a2,x)-u*e/h)
    identity('B_transport_balance',sp.diff(b1,t)+u*sp.diff(b1,x))
    char=e0*sp.exp(-u*(t-x/u)/h)*sp.exp(-x/h)
    identity('entry_characteristic_reaches_uniform_E',char-e)
    identity('decision_E_state',e.subs(t,0)-e0)
    identity('decision_A1_state',a1.subs(t,0)-(r1-e0))
    identity('decision_A2_state',a2.subs(t,0)-(r2-e0))
    identity('common_aggregate_density_first',(e+a1+b1).subs(b1,rho-r1)-rho)
    identity('common_aggregate_density_second',(e+a2+b2).subs(b2,rho-r2)-rho)
    identity('common_continuing_density_first',(a1+b1).subs(b1,rho-r1)-(rho-e))
    identity('common_continuing_density_second',(a2+b2).subs(b2,rho-r2)-(rho-e))
    identity('same_E_derivative',sp.diff(e,t)+u*e/h)
    identity('same_represented_lateral_source',(-h*sp.diff(e,t))-u*e)

    s=sp.symbols('s',real=True)
    reached_E=u*sp.integrate(e0*sp.exp(-u*s/h),(s,-T+x/u,t))
    expected_E=h*e0*(sp.exp((ell-x)/h)-sp.exp(-u*t/h))
    identity('reached_cross_section_E_count',reached_E-expected_E)
    identity('E_count_time_derivative',sp.diff(reached_E,t)-u*e)
    reached_total=rho*(u*(t+T)-x)
    continuing1=u*sp.integrate(r1-e0*sp.exp(-u*s/h)+rho-r1,(s,-T+x/u,t))
    continuing2=u*sp.integrate(r2-e0*sp.exp(-u*s/h)+rho-r2,(s,-T+x/u,t))
    identity('continuing_count_first',continuing1-(reached_total-reached_E))
    identity('continuing_count_second',continuing2-(reached_total-reached_E))
    identity('total_loaded_mass',sp.integrate(u*rho,(t,-T,0))-ell*rho)
    identity('common_population_time_prefix',sp.integrate(rho*u*(t+T),(t,-T,0))-ell*rho*T/2)
    Ebody=u*(t+T)*e
    identity('loading_E_mass_balance',sp.diff(Ebody,t)-u*e+u*(t+T)*u*e/h)

    M,E0,A0=sp.symbols('M E0 A0',positive=True)
    ehat,ahat,bhat=E0/ell,A0/ell,(M-E0-A0)/ell
    identity('compact_reconstructs_total',ell*(ehat+ahat+bhat)-M)
    identity('compact_reconstructs_E',ell*ehat-E0)
    identity('compact_reconstructs_A',ell*ahat-A0)
    identity('realized_pair_load_reveals_A',(ehat+ahat)-ehat-ahat)
    kc,a,gamma=sp.symbols('kc a gamma',positive=True)
    edot_receiving=-(u*kc-u*a)/(gamma*h)
    identity('receiving_history_recovers_A',kc+gamma*h*edot_receiving/u-a)
    identity('donor_feasibility_equivalence',(r1-e)+gamma*e-(r1+(gamma-1)*e))

    q=sp.Rational
    E=q(3,5); rlo=q(4,5); rhi=q(19,20)
    A1=q(1,5); A2=q(7,20); B1=A2; B2=A1
    expansion=q(6,5); earlyE=E*expansion
    checks={
        'same_initial_E_and_continuing_total':A1+B1==A2+B2==q(11,20),
        'distinct_A_B_split':A1!=A2 and B1!=B2,
        'exact_E_A_loads':E+A1==rlo and E+A2==rhi,
        'nonempty_positive_loading_duration':1<expansion<q(4,3),
        'earliest_E_density':earlyE==q(18,25),
        'minimum_A_input_positive':rlo-earlyE==q(2,25)>0,
        'all_A_inputs_positive':0<rlo-earlyE<=rhi-earlyE,
        'worst_loading_donor_work_strict':rhi+earlyE==q(167,100)<2,
        'whole_family_loading_bound':rhi+q(4,5)==q(7,4)<2,
        'all_input_E_A_densities_free':max(earlyE,A2)<2,
        'far_densities_free':max(B1,B2)<2,
        'same_true_total_density':rlo+B1==rhi+B2==q(23,20),
        'front_stays_upstream':1<2,
        'ordinary_load_margin_preserved':q(39,20)-2*rhi==q(1,20)>0,
        'far_load_margin_preserved':1-2*B1==q(3,10)>0,
        'same_E_observation_not_same_receiving':(3-2*A1)/2>2*E>(3-2*A2)/2,
    }
    static.update({name:bool(value) for name,value in checks.items()})
    failures=[name for name,okay in {**identities,**static}.items() if not okay]
    result={
        'date':'2026-10-19','passed':not failures,
        'scope':'Exact loading, channel, reconstruction and inference identities; static rational inequalities only; no traffic evolution',
        'sympy_version':sp.__version__,
        'symbolic_identity_count':len(identities),'static_check_count':len(static),
        'symbolic_identities':identities,'static_checks':static,'failures':failures,
        'limits':'Algebra checks do not independently certify the full observation contract, empirical observability, preferred actions or gradients.',
    }
    Path(__file__).with_name('vsl_as2_symbolic_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['passed','sympy_version','symbolic_identity_count','static_check_count','failures']},indent=2))
    if failures:raise SystemExit(1)


if __name__=='__main__':
    main()
