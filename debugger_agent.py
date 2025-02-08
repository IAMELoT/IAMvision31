# debugger_agent.py

class DebuggerAgent:
    def debug(self, code):
        """ Debugs the provided Python code. """
        try:
            exec(compile(code, 'code', 'exec'))
        except Exception as e:
            print(f"Error: {e}")