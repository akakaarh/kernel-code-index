# drivers/i2c/busses/i2c-rtl9300.c

Subsystem: drivers/i2c

## Functions (17)

### rtl9300_i2c_config_chan
- Return type: static int
- Signature: rtl9300_i2c_config_chan(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
- Line: 162

### rtl9300_i2c_config_clock
- Return type: static void
- Signature: rtl9300_i2c_config_clock(u32 clock_freq,struct rtl9300_i2c_chan * chan)
- Line: 213

### rtl9300_i2c_do_xfer
- Return type: static int
- Signature: rtl9300_i2c_do_xfer(struct rtl9300_i2c * i2c,struct rtl9300_i2c_xfer * xfer)
- Line: 329

### rtl9300_i2c_func
- Return type: static u32
- Signature: rtl9300_i2c_func(struct i2c_adapter * a)
- Line: 440

### rtl9300_i2c_init
- Return type: static int
- Signature: rtl9300_i2c_init(struct rtl9300_i2c * i2c)
- Line: 458

### rtl9300_i2c_prepare_xfer
- Return type: static int
- Signature: rtl9300_i2c_prepare_xfer(struct rtl9300_i2c * i2c,struct rtl9300_i2c_xfer * xfer)
- Line: 287

### rtl9300_i2c_probe
- Return type: static int
- Signature: rtl9300_i2c_probe(struct platform_device * pdev)
- Line: 469

### rtl9300_i2c_read
- Return type: static int
- Signature: rtl9300_i2c_read(struct rtl9300_i2c * i2c,u8 * buf,u8 len)
- Line: 244

### rtl9300_i2c_reg_addr_set
- Return type: static int
- Signature: rtl9300_i2c_reg_addr_set(struct rtl9300_i2c * i2c,u32 reg,u16 len)
- Line: 141

### rtl9300_i2c_select_scl
- Return type: static int
- Signature: rtl9300_i2c_select_scl(struct rtl9300_i2c * i2c,u8 scl)
- Line: 152

### rtl9300_i2c_smbus_xfer
- Return type: static int
- Signature: rtl9300_i2c_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 375

### rtl9300_i2c_write
- Return type: static int
- Signature: rtl9300_i2c_write(struct rtl9300_i2c * i2c,u8 * buf,u8 len)
- Line: 264

### rtl9300_i2c_writel
- Return type: static int
- Signature: rtl9300_i2c_writel(struct rtl9300_i2c * i2c,u32 data)
- Line: 282

### rtl9310_i2c_select_scl
- Return type: static int
- Signature: rtl9310_i2c_select_scl(struct rtl9300_i2c * i2c,u8 scl)
- Line: 157

### rtl9607_i2c_config_chan
- Return type: static int
- Signature: rtl9607_i2c_config_chan(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
- Line: 192

### rtl9607_i2c_config_clock
- Return type: static void
- Signature: rtl9607_i2c_config_clock(u32 clock_freq,struct rtl9300_i2c_chan * chan)
- Line: 237

### rtl9607_i2c_init
- Return type: static int
- Signature: rtl9607_i2c_init(struct rtl9300_i2c * i2c)
- Line: 464

## Structs (5)

### rtl9300_i2c
- Line: 86
- Members:
  - adap: i2c_adapter
  - i2c: rtl9300_i2c *
  - bus_freq: rtl9300_bus_freq
  - sda_num: u8
  - clk_div: u32
  - field: reg_field
  - scope: rtl9300_i2c_reg_scope
  - field_desc: rtl9300_i2c_reg_field[]
  - select_scl: int (*)(struct rtl9300_i2c * i2c,u8 scl)
  - config_chan: int (*)(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
  - config_clock: void (*)(u32 clock_freq,struct rtl9300_i2c_chan * chan)
  - misc_init: int (*)(struct rtl9300_i2c * i2c)
  - rd_reg: u32
  - wd_reg: u32
  - max_nchan: u8
  - max_data_len: u8
  - reg_addr_8bit_len: u8
  - regmap: regmap *
  - dev: device *
  - chans: rtl9300_i2c_chan[]
  - fields: regmap_field * []
  - reg_base: u32
  - rd_reg: u32
  - wd_reg: u32
  - scl_num: u8
  - sda_num: u8
  - lock: mutex
  - clk: clk *
  - type: rtl9300_i2c_xfer_type
  - dev_addr: u16
  - reg_addr: u8
  - reg_addr_len: u8
  - data: u8 *
  - data_len: u8
  - write: bool

### rtl9300_i2c_chan
- Line: 27
- Members:
  - adap: i2c_adapter
  - i2c: rtl9300_i2c *
  - bus_freq: rtl9300_bus_freq
  - sda_num: u8
  - clk_div: u32
  - field: reg_field
  - scope: rtl9300_i2c_reg_scope
  - field_desc: rtl9300_i2c_reg_field[]
  - select_scl: int (*)(struct rtl9300_i2c * i2c,u8 scl)
  - config_chan: int (*)(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
  - config_clock: void (*)(u32 clock_freq,struct rtl9300_i2c_chan * chan)
  - misc_init: int (*)(struct rtl9300_i2c * i2c)
  - rd_reg: u32
  - wd_reg: u32
  - max_nchan: u8
  - max_data_len: u8
  - reg_addr_8bit_len: u8
  - regmap: regmap *
  - dev: device *
  - chans: rtl9300_i2c_chan[]
  - fields: regmap_field * []
  - reg_base: u32
  - rd_reg: u32
  - wd_reg: u32
  - scl_num: u8
  - sda_num: u8
  - lock: mutex
  - clk: clk *
  - type: rtl9300_i2c_xfer_type
  - dev_addr: u16
  - reg_addr: u8
  - reg_addr_len: u8
  - data: u8 *
  - data_len: u8
  - write: bool

### rtl9300_i2c_drv_data
- Line: 66
- Members:
  - adap: i2c_adapter
  - i2c: rtl9300_i2c *
  - bus_freq: rtl9300_bus_freq
  - sda_num: u8
  - clk_div: u32
  - field: reg_field
  - scope: rtl9300_i2c_reg_scope
  - field_desc: rtl9300_i2c_reg_field[]
  - select_scl: int (*)(struct rtl9300_i2c * i2c,u8 scl)
  - config_chan: int (*)(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
  - config_clock: void (*)(u32 clock_freq,struct rtl9300_i2c_chan * chan)
  - misc_init: int (*)(struct rtl9300_i2c * i2c)
  - rd_reg: u32
  - wd_reg: u32
  - max_nchan: u8
  - max_data_len: u8
  - reg_addr_8bit_len: u8
  - regmap: regmap *
  - dev: device *
  - chans: rtl9300_i2c_chan[]
  - fields: regmap_field * []
  - reg_base: u32
  - rd_reg: u32
  - wd_reg: u32
  - scl_num: u8
  - sda_num: u8
  - lock: mutex
  - clk: clk *
  - type: rtl9300_i2c_xfer_type
  - dev_addr: u16
  - reg_addr: u8
  - reg_addr_len: u8
  - data: u8 *
  - data_len: u8
  - write: bool

### rtl9300_i2c_reg_field
- Line: 40
- Members:
  - adap: i2c_adapter
  - i2c: rtl9300_i2c *
  - bus_freq: rtl9300_bus_freq
  - sda_num: u8
  - clk_div: u32
  - field: reg_field
  - scope: rtl9300_i2c_reg_scope
  - field_desc: rtl9300_i2c_reg_field[]
  - select_scl: int (*)(struct rtl9300_i2c * i2c,u8 scl)
  - config_chan: int (*)(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
  - config_clock: void (*)(u32 clock_freq,struct rtl9300_i2c_chan * chan)
  - misc_init: int (*)(struct rtl9300_i2c * i2c)
  - rd_reg: u32
  - wd_reg: u32
  - max_nchan: u8
  - max_data_len: u8
  - reg_addr_8bit_len: u8
  - regmap: regmap *
  - dev: device *
  - chans: rtl9300_i2c_chan[]
  - fields: regmap_field * []
  - reg_base: u32
  - rd_reg: u32
  - wd_reg: u32
  - scl_num: u8
  - sda_num: u8
  - lock: mutex
  - clk: clk *
  - type: rtl9300_i2c_xfer_type
  - dev_addr: u16
  - reg_addr: u8
  - reg_addr_len: u8
  - data: u8 *
  - data_len: u8
  - write: bool

### rtl9300_i2c_xfer
- Line: 108
- Members:
  - adap: i2c_adapter
  - i2c: rtl9300_i2c *
  - bus_freq: rtl9300_bus_freq
  - sda_num: u8
  - clk_div: u32
  - field: reg_field
  - scope: rtl9300_i2c_reg_scope
  - field_desc: rtl9300_i2c_reg_field[]
  - select_scl: int (*)(struct rtl9300_i2c * i2c,u8 scl)
  - config_chan: int (*)(struct rtl9300_i2c * i2c,struct rtl9300_i2c_chan * chan)
  - config_clock: void (*)(u32 clock_freq,struct rtl9300_i2c_chan * chan)
  - misc_init: int (*)(struct rtl9300_i2c * i2c)
  - rd_reg: u32
  - wd_reg: u32
  - max_nchan: u8
  - max_data_len: u8
  - reg_addr_8bit_len: u8
  - regmap: regmap *
  - dev: device *
  - chans: rtl9300_i2c_chan[]
  - fields: regmap_field * []
  - reg_base: u32
  - rd_reg: u32
  - wd_reg: u32
  - scl_num: u8
  - sda_num: u8
  - lock: mutex
  - clk: clk *
  - type: rtl9300_i2c_xfer_type
  - dev_addr: u16
  - reg_addr: u8
  - reg_addr_len: u8
  - data: u8 *
  - data_len: u8
  - write: bool

## Enums (4)

### rtl9300_bus_freq
- Line: 14

### rtl9300_i2c_reg_fields
- Line: 45

### rtl9300_i2c_reg_scope
- Line: 35

### rtl9300_i2c_xfer_type
- Line: 102

## Variables (7)

- static **i2c_rtl9300_dt_ids** : const struct of_device_id[] (line 646)
- static **rtl9300_i2c_algo** : const struct i2c_algorithm (line 447)
- static **rtl9300_i2c_driver** : platform_driver (line 660)
- static **rtl9300_i2c_drv_data** : const struct rtl9300_i2c_drv_data (line 567)
- static **rtl9300_i2c_quirks** : i2c_adapter_quirks (line 452)
- static **rtl9310_i2c_drv_data** : const struct rtl9300_i2c_drv_data (line 594)
- static **rtl9607_i2c_drv_data** : const struct rtl9300_i2c_drv_data (line 621)

## Macros (29)

- **GLB_REG_FIELD**(reg,msb,lsb) (line 562)
- **MST_REG_FIELD**(reg,msb,lsb) (line 564)
- **RTL9300_I2C_MAX_DATA_LEN** (line 83)
- **RTL9300_I2C_MAX_SLOW_FREQ** (line 22)
- **RTL9300_I2C_MAX_SUPER_FAST_FREQ** (line 21)
- **RTL9300_I2C_MST_CTRL1** (line 118)
- **RTL9300_I2C_MST_CTRL2** (line 119)
- **RTL9300_I2C_MST_DATA_WORD0** (line 120)
- **RTL9300_I2C_MST_DATA_WORD1** (line 121)
- **RTL9300_I2C_MST_DATA_WORD2** (line 122)
- **RTL9300_I2C_MST_DATA_WORD3** (line 123)
- **RTL9300_I2C_MST_GLB_CTRL** (line 124)
- **RTL9300_I2C_MUX_NCHAN** (line 79)
- **RTL9300_REG_ADDR_8BIT_LEN** (line 125)
- **RTL9310_I2C_MST_CTRL** (line 129)
- **RTL9310_I2C_MST_DATA_CTRL** (line 131)
- **RTL9310_I2C_MST_IF_CTRL** (line 127)
- **RTL9310_I2C_MST_IF_SEL** (line 128)
- **RTL9310_I2C_MST_MEMADDR_CTRL** (line 130)
- **RTL9310_I2C_MUX_NCHAN** (line 80)
- **RTL9607_I2C_CONFIG** (line 133)
- **RTL9607_I2C_IND_ADR** (line 136)
- **RTL9607_I2C_IND_CMD** (line 137)
- **RTL9607_I2C_IND_RD** (line 138)
- **RTL9607_I2C_IND_WD** (line 135)
- **RTL9607_I2C_MAX_DATA_LEN** (line 84)
- **RTL9607_I2C_MUX_NCHAN** (line 81)
- **RTL9607_IO_MODE_EN** (line 134)
- **RTL9607_REG_ADDR_8BIT_LEN** (line 139)
