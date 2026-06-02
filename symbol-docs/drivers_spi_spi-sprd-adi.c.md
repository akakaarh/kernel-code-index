# drivers/spi/spi-sprd-adi.c

Subsystem: drivers/spi

## Functions (14)

### sprd_adi_check_addr
- Return type: static int
- Signature: sprd_adi_check_addr(struct sprd_adi * sadi,u32 reg)
- Line: 155

### sprd_adi_drain_fifo
- Return type: static int
- Signature: sprd_adi_drain_fifo(struct sprd_adi * sadi)
- Line: 167

### sprd_adi_fifo_is_full
- Return type: static int
- Signature: sprd_adi_fifo_is_full(struct sprd_adi * sadi)
- Line: 188

### sprd_adi_hw_init
- Return type: static void
- Signature: sprd_adi_hw_init(struct sprd_adi * sadi)
- Line: 459

### sprd_adi_probe
- Return type: static int
- Signature: sprd_adi_probe(struct platform_device * pdev)
- Line: 507

### sprd_adi_read
- Return type: static int
- Signature: sprd_adi_read(struct sprd_adi * sadi,u32 reg,u32 * read_val)
- Line: 217

### sprd_adi_read_check
- Return type: static int
- Signature: sprd_adi_read_check(u32 val,u32 addr)
- Line: 193

### sprd_adi_read_check_r2
- Return type: static int
- Signature: sprd_adi_read_check_r2(u32 val,u32 reg)
- Line: 207

### sprd_adi_read_check_r3
- Return type: static int
- Signature: sprd_adi_read_check_r3(u32 val,u32 reg)
- Line: 212

### sprd_adi_restart
- Return type: static int
- Signature: sprd_adi_restart(struct sprd_adi * sadi,unsigned long mode,const char * cmd,struct sprd_adi_wdg * wdg)
- Line: 371

### sprd_adi_restart_sc9860
- Return type: static int
- Signature: sprd_adi_restart_sc9860(struct sys_off_data * data)
- Line: 447

### sprd_adi_set_wdt_rst_mode
- Return type: static void
- Signature: sprd_adi_set_wdt_rst_mode(void * p)
- Line: 358

### sprd_adi_transfer_one
- Return type: static int
- Signature: sprd_adi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi_dev,struct spi_transfer * t)
- Line: 333

### sprd_adi_write
- Return type: static int
- Signature: sprd_adi_write(struct sprd_adi * sadi,u32 reg,u32 val)
- Line: 284

## Structs (3)

### sprd_adi
- Line: 145
- Members:
  - base: u32
  - rst_sts: u32
  - wdg_en: u32
  - wdg_clk: u32
  - slave_offset: u32
  - slave_addr_size: u32
  - read_check: int (*)(u32 val,u32 reg)
  - restart: int (*)(struct sys_off_data * data)
  - wdg_rst: void (*)(void * p)
  - ctlr: spi_controller *
  - dev: device *
  - base: void __iomem *
  - hwlock: hwspinlock *
  - slave_vbase: unsigned long
  - slave_pbase: unsigned long
  - data: const struct sprd_adi_data *

### sprd_adi_data
- Line: 137
- Members:
  - base: u32
  - rst_sts: u32
  - wdg_en: u32
  - wdg_clk: u32
  - slave_offset: u32
  - slave_addr_size: u32
  - read_check: int (*)(u32 val,u32 reg)
  - restart: int (*)(struct sys_off_data * data)
  - wdg_rst: void (*)(void * p)
  - ctlr: spi_controller *
  - dev: device *
  - base: void __iomem *
  - hwlock: hwspinlock *
  - slave_vbase: unsigned long
  - slave_pbase: unsigned long
  - data: const struct sprd_adi_data *

### sprd_adi_wdg
- Line: 130
- Members:
  - base: u32
  - rst_sts: u32
  - wdg_en: u32
  - wdg_clk: u32
  - slave_offset: u32
  - slave_addr_size: u32
  - read_check: int (*)(u32 val,u32 reg)
  - restart: int (*)(struct sys_off_data * data)
  - wdg_rst: void (*)(void * p)
  - ctlr: spi_controller *
  - dev: device *
  - base: void __iomem *
  - hwlock: hwspinlock *
  - slave_vbase: unsigned long
  - slave_pbase: unsigned long
  - data: const struct sprd_adi_data *

## Variables (5)

- static **sc9860_data** : sprd_adi_data (line 590)
- static **sc9863_data** : sprd_adi_data (line 598)
- static **sprd_adi_driver** : platform_driver (line 627)
- static **sprd_adi_of_match** : const struct of_device_id[] (line 610)
- static **ums512_data** : sprd_adi_data (line 604)

## Macros (67)

- **ADI_10BIT_SLAVE_ADDR_SIZE** (line 62)
- **ADI_10BIT_SLAVE_OFFSET** (line 63)
- **ADI_12BIT_SLAVE_ADDR_SIZE** (line 64)
- **ADI_12BIT_SLAVE_OFFSET** (line 65)
- **ADI_15BIT_SLAVE_ADDR_SIZE** (line 66)
- **ADI_15BIT_SLAVE_OFFSET** (line 67)
- **ADI_FIFO_DRAIN_TIMEOUT** (line 77)
- **ADI_HWSPINLOCK_TIMEOUT** (line 70)
- **ADI_HW_CHNS** (line 75)
- **ADI_READ_TIMEOUT** (line 78)
- **BIT_CLK_ALL_ON** (line 40)
- **BIT_FIFO_EMPTY** (line 50)
- **BIT_FIFO_FULL** (line 49)
- **BIT_RD_CMD_BUSY** (line 43)
- **BIT_WDG_EN** (line 101)
- **BIT_WDG_NEW** (line 97)
- **BIT_WDG_RST** (line 98)
- **BIT_WDG_RUN** (line 96)
- **HWRST_STATUS_ALARM** (line 113)
- **HWRST_STATUS_AUTODLOADER** (line 119)
- **HWRST_STATUS_CFTREBOOT** (line 118)
- **HWRST_STATUS_FACTORYTEST** (line 122)
- **HWRST_STATUS_FASTBOOT** (line 115)
- **HWRST_STATUS_IQMODE** (line 120)
- **HWRST_STATUS_NORMAL** (line 112)
- **HWRST_STATUS_PANIC** (line 117)
- **HWRST_STATUS_RECOVERY** (line 111)
- **HWRST_STATUS_SECURITY** (line 110)
- **HWRST_STATUS_SLEEP** (line 114)
- **HWRST_STATUS_SPECIAL** (line 116)
- **HWRST_STATUS_SPRDISK** (line 121)
- **HWRST_STATUS_WATCHDOG** (line 123)
- **PMIC_CLK_EN** (line 106)
- **PMIC_MODULE_EN** (line 105)
- **PMIC_RST_STATUS** (line 104)
- **PMIC_WDG_BASE** (line 107)
- **RDBACK_ADDR_MASK_R2** (line 85)
- **RDBACK_ADDR_MASK_R3** (line 86)
- **RDBACK_ADDR_SHIFT_R3** (line 87)
- **RD_ADDR_MASK** (line 46)
- **RD_ADDR_SHIFT** (line 44)
- **RD_VALUE_MASK** (line 45)
- **REG_ADI_ARM_CMD_STS** (line 34)
- **REG_ADI_ARM_FIFO_STS** (line 31)
- **REG_ADI_CHN_ADDR**(id) (line 36)
- **REG_ADI_CHN_EN** (line 35)
- **REG_ADI_CHN_EN1** (line 37)
- **REG_ADI_CHN_PRIH** (line 22)
- **REG_ADI_CHN_PRIL** (line 21)
- **REG_ADI_CTRL0** (line 20)
- **REG_ADI_EVT_FIFO_STS** (line 33)
- **REG_ADI_GSSI_CFG0** (line 27)
- **REG_ADI_GSSI_CFG1** (line 28)
- **REG_ADI_INT_CLR** (line 26)
- **REG_ADI_INT_EN** (line 23)
- **REG_ADI_INT_MASK** (line 25)
- **REG_ADI_INT_RAW** (line 24)
- **REG_ADI_RD_CMD** (line 29)
- **REG_ADI_RD_DATA** (line 30)
- **REG_ADI_STS** (line 32)
- **REG_WDG_CTRL** (line 92)
- **REG_WDG_LOAD_HIGH** (line 91)
- **REG_WDG_LOAD_LOW** (line 90)
- **REG_WDG_LOCK** (line 93)
- **WDG_LOAD_MASK** (line 127)
- **WDG_LOAD_VAL** (line 126)
- **WDG_UNLOCK_KEY** (line 128)
