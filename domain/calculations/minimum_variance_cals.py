import numpy as np
import math

#Functions
def calculate_correlation_matrix(assets: list) -> list:
    correlation_matrix = []
    array_size = len(assets)
    for i in range(array_size):
        correlation_matrix_row = []
        for j in range(array_size):
            correlation_matrix_row.append(np.correlate(assets[i], assets[j]))
        correlation_matrix.append(correlation_matrix_row)
    return correlation_matrix

def calculate_covariance_matrix(cor_mat: list, rr_list: list) -> list:
    covariance_matrix = []
    array_size = len(cor_mat)
    for i in range(array_size):
        covariance_matrix_row = []
        for j in range(array_size):
            covariance_matrix_row.append(rr_list[1][i] * rr_list[1][j] * cor_mat[i][j])
        covariance_matrix.append(covariance_matrix_row)
    return covariance_matrix

def calculate_weighted_vector(covariance_matrix: list) -> list:
    inverse_covariance_matrix = np.linalg.inv(covariance_matrix)
    unweighted_vector = []
    total_weight = 0
    for element in inverse_covariance_matrix:
        unweighted_vector.append(sum(element))
        total_weight += sum(element)
    weight_vector = [float(x/total_weight) for x in unweighted_vector]
    return weight_vector

def calculate_min_portfolio(weighted_matrix: list, covariance_matrix: list, expected_returns: list):
    cw_matrix = np.linalg.matmul(covariance_matrix, weighted_matrix)
    wtcw_matrix = np.dot(np.array(weighted_matrix), cw_matrix)
    return [math.sqrt(wtcw_matrix), float(np.dot(weighted_matrix, expected_returns))]

def calculate_min_risk_point_data(covariance_matrix: list, expected_returns: list, user_expected_input: float) -> list:
    inverse_covariance_matrix = np.linalg.inv(covariance_matrix)
    total_weight = 0
    for element in inverse_covariance_matrix:
        total_weight += sum(element)
    inverse_expected_sum = sum(np.linalg.matmul(inverse_covariance_matrix, expected_returns))
    inverse_expected_dot = np.dot(expected_returns, np.linalg.matmul(inverse_covariance_matrix, expected_returns))
    calc1 = total_weight*inverse_expected_dot - inverse_expected_sum**2
    calc2 = (inverse_expected_dot-user_expected_input*inverse_expected_sum)/calc1
    calc3 = (user_expected_input*total_weight - inverse_expected_sum)/calc1

    langrangian = []
    for m_element in expected_returns:
        langrangian.append(calc2 + calc3*m_element)

    weight_matrix = np.linalg.matmul(inverse_covariance_matrix, langrangian)
    risk = math.sqrt(np.dot(weight_matrix, np.linalg.matmul(covariance_matrix, weight_matrix)))

    return [weight_matrix, float(risk)]

def calculate_min_portfolio_line_data(min_weight: list, point_weight: list, cov_matrix: list, expected_returns: list, alpha_range: float, increment: float = 0.2) -> list:
    portfolio_data_sigma = []
    portfolio_data_mu = []
    starting_bound = 1 - alpha_range/2
    upper_bound = 1 + alpha_range/2

    while starting_bound <= upper_bound:
        new_weight = np.multiply(min_weight, starting_bound) + np.multiply(point_weight, 1-starting_bound)
        #[sigma, mu]
        portfolio_data_sigma.append(math.sqrt(np.dot(new_weight, np.linalg.matmul(cov_matrix, new_weight))))
        portfolio_data_mu.append(float(np.dot(new_weight, expected_returns)))
        starting_bound += increment

    return [portfolio_data_sigma, portfolio_data_mu]