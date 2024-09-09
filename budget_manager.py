def budget_manager(initial_budget):
    budget = initial_budget

    def manager(action, amount=0):
        nonlocal budget
        if action == 'add':
            budget += amount
            print(f"income : {amount}. current budget: {budget}")
        elif action == 'spend':
            if amount > budget:
                print(f"Budget is not enough, amount is {amount}، but current budget is {budget}")
            else:
                budget -= amount
                print(f"spend : {amount}. current budget: {budget}")
        elif action == 'get':
            print(f"current budget : {budget}")
            return budget
        else:
            print("unvalid operation!")

    return manager

# استفاده از سیستم مدیریت بودجه
my_budget = budget_manager(1000)

my_budget('add', 500)     # اضافه کردن ۵۰۰ به بودجه
my_budget('spend', 300)   # خرج کردن ۳۰۰ از بودجه
my_budget('get')          # گزارش بودجه فعلی
my_budget('spend', 1500)  # تلاش برای خرج بیشتر از بودجه موجود