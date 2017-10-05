#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    # Create list of tuples from NumPy arrays
    # predictions = [[123], [456], [789], ...]
    # ages = [[1.23], [4.56], [7.89], ...]
    # net_worths = [[1], [4], [7], ...]
    # ~= [(123, 1.23, 1), (456, 4.56, 4), (789, 7.89, 7)...]
    zipped_data = zip(predictions.tolist(), ages.tolist(), net_worths.tolist())
    sanitised_data = map(lambda x: (x[0][0], x[1][0], x[2][0]), zipped_data)

    # Reform data into expect return shape
    output_tuples = map(lambda x: (x[1], x[2], abs(x[0] - x[2])), sanitised_data)

    # Sort data by difference between prediction and net_worth stored in tuple
    output_tuples = sorted(output_tuples, key=lambda x: x[2])

    # Return 10 percent of points with greatest error
    elements_to_return = int(len(output_tuples) * 0.9)
    return output_tuples[:elements_to_return]
