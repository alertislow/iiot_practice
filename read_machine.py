from pymodbus.client import ModbusTcpClient
import time # 引入時間套件，用來控制頻率

def start_monitoring():
    client = ModbusTcpClient('127.0.0.1', port=502)
    
    print("🚀 監控系統啟動，按 Ctrl+C 可以停止...")
    
    try:
        while True:
            if client.connect():
                # 讀取 Address 0 的數值
                result = client.read_holding_registers(address=0)
                
                if not result.isError():
                    val = result.registers[0]
                    print(f"⏰ {time.strftime('%H:%M:%S')} | 🌡️ 目前數值：{val}")
                else:
                    print("❌ 讀取資料失敗")
                
                client.close()
            else:
                print("❌ 無法連線至機台")
            
            # 休息 2 秒再跑下一次，避免把機台操壞（或把網路塞爆）
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n🛑 監控已手動停止")

if __name__ == "__main__":
    start_monitoring()