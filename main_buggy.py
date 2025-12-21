from simulation import run_simulation

if __name__ == "__main__":
    print("=" * 60)
    print("   Симуляция библиотеки — Лабораторная работа №5 (с багами)")
    print("   Найдите и исправьте 5 ошибок с помощью отладчика")
    print("=" * 60)
    
    print("\nЗапуск №1 (seed=1):")
    run_simulation(steps=5, seed=1)
    
    print("\n" + "-"*50)
    print("Запуск №2 (тот же seed=1 — должен быть идентичен, но не будет из-за бага №5)")
    run_simulation(steps=5, seed=1)