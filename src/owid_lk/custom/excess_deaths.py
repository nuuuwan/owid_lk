from owid_lk._constants import LK_NAME


def excess_deaths(data_list):
    lk_data_list = list(
        filter(
            lambda d: d['Entity'] == LK_NAME
            and d['cumulative_estimated_daily_excess_deaths'] != '',
            data_list,
        )
    )

    latest_lk_data = lk_data_list[-1]
    date = latest_lk_data['Day']
    confirmed_deaths = (float)(
        latest_lk_data['Total confirmed deaths due to COVID-19']
    )
    excess_high = (float)(
        latest_lk_data['cumulative_estimated_daily_excess_deaths_ci_95_top']
    )
    excess_low = (float)(
        latest_lk_data['cumulative_estimated_daily_excess_deaths_ci_95_bot']
    )
    excess_high_m = excess_high / confirmed_deaths
    excess_low_m = excess_low / confirmed_deaths

    return f'''Excess #COVID19 Deaths

Confirmed Deaths: {confirmed_deaths:,.0f} ({date})

Excess Deaths: {excess_low:,.0f} to {excess_high:,.0f}

({excess_low_m:.1f}x to {excess_high_m:.1f}x of Reported)

95% CI estimated by @TheEconomist & @JohnsHopkins
    '''
