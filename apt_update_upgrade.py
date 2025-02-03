import subprocess
import time
import schedule

def system_update():
    """updates the system using apt update and apt upgrade -y"""
    try:
        update_process = subprocess.run(['sudo','apt','update'], capture_output=True, text=True, check=True)
        print("apt update output:\n", update_process.stdout)
        upgrade_process = subprocess.run(['sudo', 'apt', 'upgrade', '-y'], capture_output=True, text=True, check=True)
        print("Apt upgrade output:\n", upgrade_process.stdout)
        print("System update successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error during system update: {e}")
        print(f"Return code: {e.returncode}")
        print(f"Error output:\n{e.stderr}")   # Print stderr for debugging
    except FileNotFoundError:
        print("Error: 'sudo' or 'apt' not found.  Make sure you're on a Debian/Ubuntu-based system.")


def run_scheduled_task():
    """Schedules and runs the task repeatedly"""
    schedule.every().day.at("22:00").do(system_update)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    run_scheduled_task()
