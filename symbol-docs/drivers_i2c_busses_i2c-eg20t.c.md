# drivers/i2c/busses/i2c-eg20t.c

Subsystem: drivers/i2c

## Functions (22)

### pch_clrbit
- Return type: static void
- Signature: pch_clrbit(void __iomem * addr,u32 offset,u32 bitmask)
- Line: 190

### pch_i2c_cb
- Return type: static void
- Signature: pch_i2c_cb(struct i2c_algo_pch_data * adap)
- Line: 576

### pch_i2c_disbl_int
- Return type: static void
- Signature: pch_i2c_disbl_int(struct i2c_algo_pch_data * adap)
- Line: 701

### pch_i2c_func
- Return type: static u32
- Signature: pch_i2c_func(struct i2c_adapter * adap)
- Line: 687

### pch_i2c_handler
- Return type: static irqreturn_t
- Signature: pch_i2c_handler(int irq,void * pData)
- Line: 602

### pch_i2c_init
- Return type: static void
- Signature: pch_i2c_init(struct i2c_algo_pch_data * adap)
- Line: 202

### pch_i2c_probe
- Return type: static int
- Signature: pch_i2c_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 712

### pch_i2c_readbytes
- Return type: static s32
- Signature: pch_i2c_readbytes(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,u32 last,u32 first)
- Line: 474

### pch_i2c_remove
- Return type: static void
- Signature: pch_i2c_remove(struct pci_dev * pdev)
- Line: 808

### pch_i2c_repstart
- Return type: static void
- Signature: pch_i2c_repstart(struct i2c_algo_pch_data * adap)
- Line: 346

### pch_i2c_restart
- Return type: static void
- Signature: pch_i2c_restart(struct i2c_algo_pch_data * adap)
- Line: 460

### pch_i2c_resume
- Return type: static int __maybe_unused
- Signature: pch_i2c_resume(struct device * dev)
- Line: 860

### pch_i2c_sendack
- Return type: static void
- Signature: pch_i2c_sendack(struct i2c_algo_pch_data * adap)
- Line: 436

### pch_i2c_sendnack
- Return type: static void
- Signature: pch_i2c_sendnack(struct i2c_algo_pch_data * adap)
- Line: 447

### pch_i2c_start
- Return type: static void
- Signature: pch_i2c_start(struct i2c_algo_pch_data * adap)
- Line: 289

### pch_i2c_stop
- Return type: static void
- Signature: pch_i2c_stop(struct i2c_algo_pch_data * adap)
- Line: 300

### pch_i2c_suspend
- Return type: static int __maybe_unused
- Signature: pch_i2c_suspend(struct device * dev)
- Line: 832

### pch_i2c_wait_for_bus_idle
- Return type: static s32
- Signature: pch_i2c_wait_for_bus_idle(struct i2c_algo_pch_data * adap,s32 timeout)
- Line: 253

### pch_i2c_wait_for_check_xfer
- Return type: static int
- Signature: pch_i2c_wait_for_check_xfer(struct i2c_algo_pch_data * adap)
- Line: 308

### pch_i2c_writebytes
- Return type: static s32
- Signature: pch_i2c_writebytes(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,u32 last,u32 first)
- Line: 363

### pch_i2c_xfer
- Return type: static s32
- Signature: pch_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,s32 num)
- Line: 636

### pch_setbit
- Return type: static void
- Signature: pch_setbit(void __iomem * addr,u32 offset,u32 bitmask)
- Line: 182

## Structs (2)

### adapter_info
- Line: 154
- Members:
  - pch_adapter: i2c_adapter
  - p_adapter_info: adapter_info *
  - pch_base_address: void __iomem *
  - pch_buff_mode_en: int
  - pch_event_flag: u32
  - pch_i2c_xfer_in_progress: bool
  - pch_data: i2c_algo_pch_data[]
  - pch_i2c_suspended: bool
  - ch_num: int

### i2c_algo_pch_data
- Line: 135
- Members:
  - pch_adapter: i2c_adapter
  - p_adapter_info: adapter_info *
  - pch_base_address: void __iomem *
  - pch_buff_mode_en: int
  - pch_event_flag: u32
  - pch_i2c_xfer_in_progress: bool
  - pch_data: i2c_algo_pch_data[]
  - pch_i2c_suspended: bool
  - ch_num: int

## Variables (6)

- static **pch_algorithm** : const struct i2c_algorithm (line 692)
- static **pch_clk** : int (line 162)
- static **pch_event** : wait_queue_head_t (line 163)
- static **pch_i2c_speed** : int (line 161)
- static **pch_pcidev_id** : const struct pci_device_id[] (line 171)
- static **pch_pcidriver** : pci_driver (line 875)

## Macros (88)

- **BUFFER_MODE** (line 88)
- **BUFFER_MODE_INTR_DISBL** (line 86)
- **BUFFER_MODE_INTR_ENBL** (line 85)
- **BUFFER_MODE_MASK** (line 74)
- **BUF_LEN_MAX** (line 79)
- **BUS_IDLE_TIMEOUT** (line 49)
- **CLR_REG** (line 58)
- **EEPROM_RST_INTR_DISBL** (line 84)
- **EEPROM_RST_INTR_ENBL** (line 83)
- **EEPROM_SR_MODE** (line 89)
- **EEPROM_SW_RST_MODE** (line 81)
- **FAST_MODE_CLK** (line 76)
- **FAST_MODE_EN** (line 77)
- **I2CBMAG_BIT** (line 72)
- **I2CBMAL_BIT** (line 63)
- **I2CBMAL_EVENT** (line 98)
- **I2CBMDZ_BIT** (line 71)
- **I2CBMFI_BIT** (line 62)
- **I2CBMFI_EVENT** (line 97)
- **I2CBMIS_BIT** (line 66)
- **I2CBMIS_EVENT** (line 101)
- **I2CBMNA_BIT** (line 64)
- **I2CBMNA_EVENT** (line 99)
- **I2CBMTO_BIT** (line 65)
- **I2CBMTO_EVENT** (line 100)
- **I2CESRFIIE_BIT** (line 69)
- **I2CESRFI_BIT** (line 67)
- **I2CESRFI_EVENT** (line 102)
- **I2CESRTOIE_BIT** (line 70)
- **I2CESRTO_BIT** (line 68)
- **I2CESRTO_EVENT** (line 103)
- **I2CMAL_BIT** (line 61)
- **I2CMAL_EVENT** (line 95)
- **I2CMBB_BIT** (line 73)
- **I2CMCF_BIT** (line 59)
- **I2CMCF_EVENT** (line 96)
- **I2CMIF_BIT** (line 60)
- **I2C_ERROR_MASK** (line 93)
- **I2C_TX_MODE** (line 90)
- **NORMAL_INTR_ENBL** (line 82)
- **NORMAL_MODE** (line 87)
- **PCH_ACK** (line 56)
- **PCH_BUFFER_MODE** (line 80)
- **PCH_BUFFER_MODE_ENABLE** (line 24)
- **PCH_BUFF_START** (line 54)
- **PCH_BUF_RD** (line 92)
- **PCH_BUF_TX** (line 91)
- **PCH_EEPROM_SW_RST_MODE_ENABLE** (line 25)
- **PCH_ESR_START** (line 53)
- **PCH_EVENT_NONE** (line 22)
- **PCH_EVENT_SET** (line 21)
- **PCH_GETACK** (line 57)
- **PCH_I2CBC** (line 32)
- **PCH_I2CBUFCTL** (line 37)
- **PCH_I2CBUFFOR** (line 36)
- **PCH_I2CBUFLEV** (line 40)
- **PCH_I2CBUFMSK** (line 38)
- **PCH_I2CBUFSLV** (line 34)
- **PCH_I2CBUFSTA** (line 39)
- **PCH_I2CBUFSUB** (line 35)
- **PCH_I2CCTL** (line 28)
- **PCH_I2CCTL_I2CMEN** (line 50)
- **PCH_I2CDR** (line 30)
- **PCH_I2CESRCTL** (line 42)
- **PCH_I2CESRFOR** (line 41)
- **PCH_I2CESRMSK** (line 43)
- **PCH_I2CESRSTA** (line 44)
- **PCH_I2CMOD** (line 33)
- **PCH_I2CMON** (line 31)
- **PCH_I2CNF** (line 47)
- **PCH_I2CSADR** (line 27)
- **PCH_I2CSR** (line 29)
- **PCH_I2CSRST** (line 46)
- **PCH_I2CTMR** (line 45)
- **PCH_I2C_MAX_DEV** (line 124)
- **PCH_MAX_CLK** (line 23)
- **PCH_REPSTART** (line 55)
- **PCH_RESTART** (line 52)
- **PCH_START** (line 51)
- **PCI_DEVICE_ID_ML7213_I2C** (line 167)
- **PCI_DEVICE_ID_ML7223_I2C** (line 168)
- **PCI_DEVICE_ID_ML7831_I2C** (line 169)
- **PCI_DEVICE_ID_PCH_I2C** (line 104)
- **SUB_ADDR_LEN_MAX** (line 78)
- **pch_dbg**(adap,fmt,arg...) (line 106)
- **pch_err**(adap,fmt,arg...) (line 109)
- **pch_pci_dbg**(pdev,fmt,arg...) (line 115)
- **pch_pci_err**(pdev,fmt,arg...) (line 112)
