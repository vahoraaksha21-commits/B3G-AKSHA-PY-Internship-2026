def task_status():
    status="pending"

    def update_status():
        nonlocal status
        print("Updating Task Status...")
        status="Completed"

    print("Initial Status :",status)
    update_status()
    print("Final Status :",status)

task_status()