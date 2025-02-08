class TestExecutionAgent:
  def __init__(self, name):
      self.name = name
      self.test_results = []

  def run_test(self, test_case):
      result = test_case()
      self.test_results.append(result)
      print(f"[{self.name}] Test Result: {result}")

  def report_results(self):
      print(f"[{self.name}] Final Test Results: {self.test_results}")