from DataManager.data_manager import DataManager


if __name__ == "__main__":
    dm = DataManager()

    cpi = dm.get_cpi()
    print(f"CPI: {cpi}")
