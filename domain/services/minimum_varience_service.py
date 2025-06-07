from domain.calculations import minimum_variance_cals as min_var

def current_minimum_variance_service(correlation: list, assets: list, expected_return: float) -> dict:
    covariance = min_var.calculate_covariance_matrix(cor_mat=correlation, rr_list=assets)
    weights = min_var.calculate_weighted_vector(covariance_matrix=covariance)

    minimum_portfolio = min_var.calculate_min_portfolio(
        weighted_matrix=weights, covariance_matrix=covariance, expected_returns=assets[0]
    )

    minimum_risk = min_var.calculate_min_risk_point_data(
        covariance_matrix=covariance, expected_returns=assets[0], user_expected_input=expected_return
    )

    complete_graph = min_var.calculate_min_portfolio_line_data(
        min_weight=weights, point_weight=minimum_risk[0], cov_matrix=covariance, expected_returns=assets[0],
        alpha_range=13.6, increment=0.2
    )

    combination_dict = {
        "Minimum Portfolio": minimum_portfolio,
        "Minimum Frontier": complete_graph
    }

    return combination_dict

if __name__ == "__main__":
    testER = [[0.08, 0.075, 0.09, 0.065, 0.1, 0.07, 0.085], [0.15, 0.12, 0.18, 0.10, 0.20, 0.11, 0.16]]
    testCor = [[1, 0.8, 0.6, 0.3, 0.7, 0.5, 0.65],
               [0.8, 1, 0.55, 0.4, 0.6, 0.45, 0.5],
               [0.6, 0.55, 1, 0.35, 0.75, 0.5, 0.6],
               [0.3, 0.4, 0.35, 1, 0.25, 0.3, 0.2],
               [0.7, 0.6, 0.75, 0.25, 1, 0.55, 0.65],
               [0.5, 0.45, 0.5, 0.3, 0.55, 1, 0.4],
               [0.65, 0.5, 0.6, 0.2, 0.65, 0.4, 1]]
    expectedreturn = 0.08

    # current_minimum_variance_service(testCor, testER, expectedreturn)

    print(current_minimum_variance_service(testCor, testER, expectedreturn))