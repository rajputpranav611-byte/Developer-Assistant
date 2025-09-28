from threading import Thread
import time, os

# --- Agent 1: Code Reviewer ---
def code_reviewer(file):
    try:
        with open(file) as f:
            text = f.read()
        if "TODO" in text:
            return "⚠️ Code Reviewer: Found TODO comments."
        elif "print(" not in text:
            return "ℹ️ Code Reviewer: No print statements found."
        else:
            return "✅ Code Reviewer: Looks clean."
    except Exception as e:
        return f"❌ Code Reviewer Error: {e}"

# --- Agent 2: Test Runner ---
def test_runner(file):
    try:
        exec(open(file).read())
        return "✅ Test Runner: Script ran successfully."
    except Exception as e:
        return f"❌ Test Runner: Failed with error: {e}"

# --- Continuous Loop Monitor ---
def loop_monitor():
    last_seen = None
    print("🚀 Autonomous Developer Assistant started. Monitoring 'main.py' ...\n")
    while True:
        if os.path.exists("main.py"):
            mtime = os.path.getmtime("main.py")
            if mtime != last_seen:  # file changed
                last_seen = mtime
                print("\n🔄 Change detected in main.py! Running agents in parallel...\n")

                # Run agents in parallel
                t1 = Thread(target=lambda: print(code_reviewer("main.py")))
                t2 = Thread(target=lambda: print(test_runner("main.py")))
                t1.start(); t2.start()
                t1.join(); t2.join()

        time.sleep(5)  # checks every 5 seconds

if __name__ == "__main__":
    loop_monitor()
