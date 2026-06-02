# drivers/i2c/busses/i2c-nomadik.c

Subsystem: drivers/i2c

## Functions (29)

### clear_all_interrupts
- Return type: static void
- Signature: clear_all_interrupts(struct nmk_i2c_dev * priv)
- Line: 309

### disable_all_interrupts
- Return type: static void
- Signature: disable_all_interrupts(struct nmk_i2c_dev * priv)
- Line: 300

### disable_interrupts
- Return type: static int
- Signature: disable_interrupts(struct nmk_i2c_dev * priv,u32 irq)
- Line: 757

### fill_tx_fifo
- Return type: static void
- Signature: fill_tx_fifo(struct nmk_i2c_dev * priv,int no_bytes)
- Line: 546

### flush_i2c_fifo
- Return type: static int
- Signature: flush_i2c_fifo(struct nmk_i2c_dev * priv)
- Line: 264

### i2c_clr_bit
- Return type: static void
- Signature: i2c_clr_bit(void __iomem * reg,u32 mask)
- Line: 234

### i2c_irq_handler
- Return type: static irqreturn_t
- Signature: i2c_irq_handler(int irq,void * arg)
- Line: 776

### i2c_set_bit
- Return type: static void
- Signature: i2c_set_bit(void __iomem * reg,u32 mask)
- Line: 229

### init_hw
- Return type: static int
- Signature: init_hw(struct nmk_i2c_dev * priv)
- Line: 318

### load_i2c_mcr_reg
- Return type: static u32
- Signature: load_i2c_mcr_reg(struct nmk_i2c_dev * priv,u16 flags)
- Line: 350

### nmk_i2c_exit
- Return type: static void __exit
- Signature: nmk_i2c_exit(void)
- Line: 1228

### nmk_i2c_eyeq5_probe
- Return type: static int
- Signature: nmk_i2c_eyeq5_probe(struct nmk_i2c_dev * priv)
- Line: 1039

### nmk_i2c_functionality
- Return type: static unsigned int
- Signature: nmk_i2c_functionality(struct i2c_adapter * adap)
- Line: 994

### nmk_i2c_init
- Return type: static int __init
- Signature: nmk_i2c_init(void)
- Line: 1223

### nmk_i2c_of_probe
- Return type: static void
- Signature: nmk_i2c_of_probe(struct device_node * np,struct nmk_i2c_dev * priv)
- Line: 1004

### nmk_i2c_probe
- Return type: static int
- Signature: nmk_i2c_probe(struct amba_device * adev,const struct amba_id * id)
- Line: 1082

### nmk_i2c_readb
- Return type: static u8
- Signature: nmk_i2c_readb(const struct nmk_i2c_dev * priv,unsigned long reg)
- Line: 239

### nmk_i2c_remove
- Return type: static void
- Signature: nmk_i2c_remove(struct amba_device * adev)
- Line: 1175

### nmk_i2c_resume_early
- Return type: static int
- Signature: nmk_i2c_resume_early(struct device * dev)
- Line: 951

### nmk_i2c_runtime_resume
- Return type: static int
- Signature: nmk_i2c_runtime_resume(struct device * dev)
- Line: 966

### nmk_i2c_runtime_suspend
- Return type: static int
- Signature: nmk_i2c_runtime_suspend(struct device * dev)
- Line: 956

### nmk_i2c_suspend_late
- Return type: static int
- Signature: nmk_i2c_suspend_late(struct device * dev)
- Line: 939

### nmk_i2c_wait_xfer_done
- Return type: static bool
- Signature: nmk_i2c_wait_xfer_done(struct nmk_i2c_dev * priv)
- Line: 480

### nmk_i2c_writeb
- Return type: static void
- Signature: nmk_i2c_writeb(const struct nmk_i2c_dev * priv,u32 val,unsigned long reg)
- Line: 248

### nmk_i2c_xfer
- Return type: static int
- Signature: nmk_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num_msgs)
- Line: 713

### nmk_i2c_xfer_one
- Return type: static int
- Signature: nmk_i2c_xfer_one(struct nmk_i2c_dev * priv,u16 flags)
- Line: 631

### read_i2c
- Return type: static int
- Signature: read_i2c(struct nmk_i2c_dev * priv,u16 flags)
- Line: 505

### setup_i2c_controller
- Return type: static void
- Signature: setup_i2c_controller(struct nmk_i2c_dev * priv)
- Line: 399

### write_i2c
- Return type: static int
- Signature: write_i2c(struct nmk_i2c_dev * priv,u16 flags)
- Line: 570

## Structs (3)

### i2c_nmk_client
- Line: 170
- Members:
  - has_mtdws: bool
  - fifodepth: u32
  - slave_adr: unsigned short
  - count: unsigned long
  - buffer: unsigned char *
  - xfer_bytes: unsigned long
  - operation: i2c_operation
  - vendor: i2c_vendor_data *
  - adev: amba_device *
  - adap: i2c_adapter
  - irq: int
  - virtbase: void __iomem *
  - clk: clk *
  - cli: i2c_nmk_client
  - clk_freq: u32
  - tft: unsigned char
  - rft: unsigned char
  - timeout_usecs: u32
  - sm: i2c_freq_mode
  - stop: int
  - xfer_wq: wait_queue_head
  - xfer_done: bool
  - result: int
  - has_32b_bus: bool

### i2c_vendor_data
- Line: 137
- Members:
  - has_mtdws: bool
  - fifodepth: u32
  - slave_adr: unsigned short
  - count: unsigned long
  - buffer: unsigned char *
  - xfer_bytes: unsigned long
  - operation: i2c_operation
  - vendor: i2c_vendor_data *
  - adev: amba_device *
  - adap: i2c_adapter
  - irq: int
  - virtbase: void __iomem *
  - clk: clk *
  - cli: i2c_nmk_client
  - clk_freq: u32
  - tft: unsigned char
  - rft: unsigned char
  - timeout_usecs: u32
  - sm: i2c_freq_mode
  - stop: int
  - xfer_wq: wait_queue_head
  - xfer_done: bool
  - result: int
  - has_32b_bus: bool

### nmk_i2c_dev
- Line: 198
- Members:
  - has_mtdws: bool
  - fifodepth: u32
  - slave_adr: unsigned short
  - count: unsigned long
  - buffer: unsigned char *
  - xfer_bytes: unsigned long
  - operation: i2c_operation
  - vendor: i2c_vendor_data *
  - adev: amba_device *
  - adap: i2c_adapter
  - irq: int
  - virtbase: void __iomem *
  - clk: clk *
  - cli: i2c_nmk_client
  - clk_freq: u32
  - tft: unsigned char
  - rft: unsigned char
  - timeout_usecs: u32
  - sm: i2c_freq_mode
  - stop: int
  - xfer_wq: wait_queue_head
  - xfer_done: bool
  - result: int
  - has_32b_bus: bool

## Enums (5)

### i2c_eyeq5_speed
- Line: 126

### i2c_freq_mode
- Line: 116

### i2c_operating_mode
- Line: 156

### i2c_operation
- Line: 150

### i2c_status
- Line: 142

## Variables (9)

- static **abort_causes** : const char * [] (line 219)
- static **nmk_i2c_algo** : const struct i2c_algorithm (line 999)
- static **nmk_i2c_driver** : amba_driver (line 1213)
- static **nmk_i2c_eyeq5_masks** : const unsigned int[] (line 1031)
- static **nmk_i2c_eyeq_match_table** : const struct of_device_id[] (line 1070)
- static **nmk_i2c_ids** : const struct amba_id[] (line 1197)
- static **nmk_i2c_pm** : const struct dev_pm_ops (line 989)
- static **vendor_db8500** : i2c_vendor_data (line 1192)
- static **vendor_stn8815** : i2c_vendor_data (line 1187)

## Macros (67)

- **ADR_3MSB_BITS** (line 343)
- **DEFAULT_I2C_REG_CR** (line 340)
- **DRIVER_NAME** (line 36)
- **I2C_BRCR** (line 49)
- **I2C_BRCR_BRCNT1** (line 90)
- **I2C_BRCR_BRCNT2** (line 91)
- **I2C_CLEAR_ALL_INTS** (line 111)
- **I2C_CR** (line 39)
- **I2C_CR_DMA_RX_EN** (line 64)
- **I2C_CR_DMA_SLE** (line 65)
- **I2C_CR_DMA_TX_EN** (line 63)
- **I2C_CR_FON** (line 67)
- **I2C_CR_FRX** (line 62)
- **I2C_CR_FS** (line 68)
- **I2C_CR_FTX** (line 61)
- **I2C_CR_LM** (line 66)
- **I2C_CR_OM** (line 57)
- **I2C_CR_PE** (line 56)
- **I2C_CR_SAM** (line 58)
- **I2C_CR_SGCM** (line 60)
- **I2C_CR_SM** (line 59)
- **I2C_DMAR** (line 48)
- **I2C_HSMCR** (line 41)
- **I2C_ICR** (line 53)
- **I2C_IMSCR** (line 50)
- **I2C_IT_BERR** (line 107)
- **I2C_IT_MAL** (line 106)
- **I2C_IT_MTD** (line 104)
- **I2C_IT_MTDWS** (line 108)
- **I2C_IT_RFSE** (line 102)
- **I2C_IT_RFSR** (line 101)
- **I2C_IT_RXFE** (line 98)
- **I2C_IT_RXFF** (line 100)
- **I2C_IT_RXFNF** (line 99)
- **I2C_IT_STD** (line 105)
- **I2C_IT_TXFE** (line 94)
- **I2C_IT_TXFF** (line 96)
- **I2C_IT_TXFNE** (line 95)
- **I2C_IT_TXFOVR** (line 97)
- **I2C_IT_WTSR** (line 103)
- **I2C_MCR** (line 42)
- **I2C_MCR_A7** (line 75)
- **I2C_MCR_AM** (line 78)
- **I2C_MCR_EA10** (line 76)
- **I2C_MCR_LENGTH** (line 80)
- **I2C_MCR_OP** (line 74)
- **I2C_MCR_SB** (line 77)
- **I2C_MCR_STOP** (line 79)
- **I2C_MISR** (line 52)
- **I2C_RFR** (line 45)
- **I2C_RFTR** (line 47)
- **I2C_RISR** (line 51)
- **I2C_SCR** (line 40)
- **I2C_SCR_SLSU** (line 71)
- **I2C_SR** (line 44)
- **I2C_SR_CAUSE** (line 85)
- **I2C_SR_LENGTH** (line 87)
- **I2C_SR_OP** (line 83)
- **I2C_SR_STATUS** (line 84)
- **I2C_SR_TYPE** (line 86)
- **I2C_TFR** (line 43)
- **I2C_TFTR** (line 46)
- **LOOP_ATTEMPTS** (line 266)
- **MAX_I2C_FIFO_THRESHOLD** (line 114)
- **NMK_I2C_EYEQ5_OLB_IOCR2** (line 124)
- **NMK_I2C_EYEQ_FLAG_32B_BUS** (line 1067)
- **NMK_I2C_EYEQ_FLAG_IS_EYEQ5** (line 1068)
