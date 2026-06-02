# drivers/i2c/busses/i2c-cht-wc.c

Subsystem: drivers/i2c

## Functions (12)

### cht_wc_i2c_adap_func
- Return type: static u32
- Signature: cht_wc_i2c_adap_func(struct i2c_adapter * adap)
- Line: 109

### cht_wc_i2c_adap_i2c_probe
- Return type: static int
- Signature: cht_wc_i2c_adap_i2c_probe(struct platform_device * pdev)
- Line: 426

### cht_wc_i2c_adap_i2c_remove
- Return type: static void
- Signature: cht_wc_i2c_adap_i2c_remove(struct platform_device * pdev)
- Line: 532

### cht_wc_i2c_adap_lock_bus
- Return type: static void
- Signature: cht_wc_i2c_adap_lock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 196

### cht_wc_i2c_adap_smbus_xfer
- Return type: static int
- Signature: cht_wc_i2c_adap_smbus_xfer(struct i2c_adapter * _adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 115

### cht_wc_i2c_adap_thread_handler
- Return type: static irqreturn_t
- Signature: cht_wc_i2c_adap_thread_handler(int id,void * data)
- Line: 57

### cht_wc_i2c_adap_trylock_bus
- Return type: static int
- Signature: cht_wc_i2c_adap_trylock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 202

### cht_wc_i2c_adap_unlock_bus
- Return type: static void
- Signature: cht_wc_i2c_adap_unlock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 208

### cht_wc_i2c_irq_disable
- Return type: static void
- Signature: cht_wc_i2c_irq_disable(struct irq_data * data)
- Line: 252

### cht_wc_i2c_irq_enable
- Return type: static void
- Signature: cht_wc_i2c_irq_enable(struct irq_data * data)
- Line: 245

### cht_wc_i2c_irq_lock
- Return type: static void
- Signature: cht_wc_i2c_irq_lock(struct irq_data * data)
- Line: 221

### cht_wc_i2c_irq_sync_unlock
- Return type: static void
- Signature: cht_wc_i2c_irq_sync_unlock(struct irq_data * data)
- Line: 228

## Structs (1)

### cht_wc_i2c_adap
- Line: 40
- Members:
  - adapter: i2c_adapter
  - wait: wait_queue_head_t
  - irqchip: irq_chip
  - adap_lock: mutex
  - irqchip_lock: mutex
  - regmap: regmap *
  - irq_domain: irq_domain *
  - client: i2c_client *
  - client_irq: int
  - irq_mask: u8
  - old_irq_mask: u8
  - read_data: int
  - io_error: bool
  - done: bool

## Variables (26)

- static **bq24190_node** : const struct software_node (line 278)
- static **bq24190_pdata** : bq24190_platform_data (line 298)
- static **bq24190_props** : const struct property_entry[] (line 271)
- static **bq24190_suppliers** : const char * const[] (line 268)
- static **bq24190_vbus_init_data** : const struct regulator_init_data (line 288)
- static **bq2589x_pdata** : bq25890_platform_data (line 324)
- static **bq2589x_vbus_consumer** : regulator_consumer_supply (line 311)
- static **bq2589x_vbus_init_data** : const struct regulator_init_data (line 316)
- static **cht_wc_i2c_adap_algo** : const struct i2c_algorithm (line 170)
- static **cht_wc_i2c_adap_driver** : platform_driver (line 547)
- static **cht_wc_i2c_adap_id_table** : const struct platform_device_id[] (line 541)
- static **cht_wc_i2c_adap_lock_ops** : const struct i2c_lock_operations (line 214)
- static **cht_wc_i2c_irq_chip** : const struct irq_chip (line 259)
- static **fusb302_consumer** : regulator_consumer_supply (line 282)
- static **gpd_win_board_info** : i2c_board_info (line 302)
- static **lenovo_yb1_bq25892_node** : const struct software_node (line 371)
- static **lenovo_yb1_bq25892_props** : const struct property_entry[] (line 349)
- static **lenovo_yb1_bq25892_suppliers** : const char * const[] (line 347)
- static **lenovo_yoga_tab3_board_info** : i2c_board_info (line 418)
- static **lenovo_yogabook1_board_info** : i2c_board_info (line 375)
- static **lenovo_yt3_bq25892_1_node** : const struct software_node (line 413)
- static **lenovo_yt3_bq25892_1_props** : const struct property_entry[] (line 390)
- static **lenovo_yt3_bq25892_1_suppliers** : const char * const[] (line 384)
- static **xiaomi_mipad2_board_info** : i2c_board_info (line 338)
- static **xiaomi_mipad2_node** : const struct software_node (line 334)
- static **xiaomi_mipad2_props** : const struct property_entry[] (line 328)

## Macros (14)

- **CHT_WC_EXTCHGRIRQ** (line 32)
- **CHT_WC_EXTCHGRIRQ_ADAP_IRQMASK** (line 37)
- **CHT_WC_EXTCHGRIRQ_CLIENT_IRQ** (line 33)
- **CHT_WC_EXTCHGRIRQ_MSK** (line 38)
- **CHT_WC_EXTCHGRIRQ_NACK_IRQ** (line 36)
- **CHT_WC_EXTCHGRIRQ_READ_IRQ** (line 35)
- **CHT_WC_EXTCHGRIRQ_WRITE_IRQ** (line 34)
- **CHT_WC_I2C_CLIENT_ADDR** (line 27)
- **CHT_WC_I2C_CTRL** (line 24)
- **CHT_WC_I2C_CTRL_RD** (line 26)
- **CHT_WC_I2C_CTRL_WR** (line 25)
- **CHT_WC_I2C_RDDATA** (line 30)
- **CHT_WC_I2C_REG_OFFSET** (line 28)
- **CHT_WC_I2C_WRDATA** (line 29)
