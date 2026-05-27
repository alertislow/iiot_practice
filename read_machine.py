from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', port=502)

if client.connect():
    print("✅ 連線成功！")
    
    # 試試看完全只傳 address，這在 3.x 版中通常會讀取 count=1
    # 或是明確指定 address=0
    result = client.read_holding_registers(address=0)
    
    if not result.isError():
        print(f"📊 讀取到的數值是：{result.registers[0]}")
    else:
        print("❌ 讀取失敗，請檢查模擬器設定")
    
    client.close()
else:
    print("❌ 無法連線到模擬器")