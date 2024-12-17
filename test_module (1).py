import unittest
import medical_data_visualizer
import matplotlib as mpl


# Test case for the Categorical Plot
class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        """
        Setup method to initialize the figure and axis of the categorical plot.
        This method runs before every test in the CatPlotTestCase class.
        """
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]  # Access the first axis of the figure.

    def test_line_plot_labels(self):
        """
        Test to verify the x-axis and y-axis labels, as well as the x-tick labels,
        for the categorical plot.
        """
        # Check the x-axis label
        actual = self.ax.get_xlabel()
        expected = "variable"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'variable'")

        # Check the y-axis label
        actual = self.ax.get_ylabel()
        expected = "total"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'total'")

        # Check the x-tick labels
        actual = []
        for label in self.ax.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        expected = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(
            actual, expected, 
            "Expected bar plot secondary x labels to be 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'"
        )

    def test_bar_plot_number_of_bars(self):
        """
        Test to verify the number of bars (rectangles) present in the categorical plot.
        """
        # Count the number of Rectangle objects (bars) in the plot
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 13  # Expected number of bars
        self.assertEqual(actual, expected, "Expected a different number of bars chart.")


# Test case for the Heat Map
class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        """
        Setup method to initialize the figure and axis of the heat map.
        This method runs before every test in the HeatMapTestCase class.
        """
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]  # Access the first axis of the figure.

    def test_heat_map_labels(self):
        """
        Test to verify the x-tick labels of the heat map.
        """
        # Retrieve the x-tick labels as a list
        actual = []
        for label in self.ax.get_xticklabels():
            actual.append(label.get_text())
        
        # Expected labels on the heat map
        expected = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 
                    'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(
            actual, expected, 
            "Expected heat map labels to be 'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', "
            "'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'."
        )
    
    def test_heat_map_values(self):
        """
        Test to verify the values displayed on the heat map.
        It checks whether the numeric values on the heat map match the expected values.
        """
        # Retrieve all the text elements displayed in the heat map (correlation values)
        actual = [text.get_text() for text in self.ax.get_default_bbox_extra_artists() 
                  if isinstance(text, mpl.text.Text)]
        print(actual)  # For debugging purposes

        # Expected values to appear on the heat map
        expected = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', 
                    '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', 
                    '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', 
                    '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', 
                    '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', 
                    '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', 
                    '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        
        self.assertEqual(
            actual, expected, 
            "Expected different values in heat map."
        )


# Run the tests if the script is executed directly
if __name__ == "__main__":
    unittest.main()
