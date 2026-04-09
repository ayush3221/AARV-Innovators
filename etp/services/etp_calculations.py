def calculate_treatment(data):
    # Treatment Efficiency Reductions
    # BOD/COD/TSS reduction (nested stages)
    bod_f = data['bod'] * 0.70 * 0.15 * 0.90 
    cod_f = data['cod'] * 0.25 * 0.80
    tss_f = data['tss'] * 0.40 * 0.20
    ph_f = 7.0 + (data['ph'] - 7.0) * 0.2

    # New Chemicals logic
    og_f = data['oil_grease'] * 0.10   # 90% removal
    cn_f = data['cyanide'] * 0.02      # 98% removal
    an_f = data['ammonical_n'] * 0.20  # 80% removal

    # CPCB Standards Compliance Check
    is_compliant = (
        bod_f < 30 and 
        cod_f < 250 and 
        tss_f < 100 and 
        5.5 <= ph_f <= 9.0 and 
        og_f < 10 and 
        cn_f < 0.2 and 
        an_f < 50
    )

    return {
        "bod_out": round(bod_f, 2),
        "cod_out": round(cod_f, 2),
        "tss_out": round(tss_f, 2),
        "ph_out": round(ph_f, 2),
        "og_out": round(og_f, 2),
        "cn_out": round(cn_f, 4),
        "an_out": round(an_f, 2),
        "compliance": "PASSED" if is_compliant else "FAILED"
    }