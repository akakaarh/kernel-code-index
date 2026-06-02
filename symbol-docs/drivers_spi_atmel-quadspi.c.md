# drivers/spi/atmel-quadspi.c

Subsystem: drivers/spi

## Functions (38)

### atmel_qspi_dma_callback
- Return type: static void
- Signature: atmel_qspi_dma_callback(void * param)
- Line: 767

### atmel_qspi_dma_init
- Return type: static int
- Signature: atmel_qspi_dma_init(struct spi_controller * ctrl)
- Line: 1306

### atmel_qspi_dma_rx_xfer
- Return type: static int
- Signature: atmel_qspi_dma_rx_xfer(struct spi_mem * mem,const struct spi_mem_op * op,struct sg_table * sgt,loff_t loff)
- Line: 811

### atmel_qspi_dma_transfer
- Return type: static int
- Signature: atmel_qspi_dma_transfer(struct spi_mem * mem,const struct spi_mem_op * op,loff_t loff)
- Line: 861

### atmel_qspi_dma_tx_xfer
- Return type: static int
- Signature: atmel_qspi_dma_tx_xfer(struct spi_mem * mem,const struct spi_mem_op * op,struct sg_table * sgt,loff_t loff)
- Line: 836

### atmel_qspi_dma_xfer
- Return type: static int
- Signature: atmel_qspi_dma_xfer(struct atmel_qspi * aq,struct dma_chan * chan,dma_addr_t dma_dst,dma_addr_t dma_src,unsigned int len)
- Line: 774

### atmel_qspi_exec_op
- Return type: static int
- Signature: atmel_qspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 944

### atmel_qspi_find_mode
- Return type: static int
- Signature: atmel_qspi_find_mode(const struct spi_mem_op * op)
- Line: 458

### atmel_qspi_get_name
- Return type: static const char *
- Signature: atmel_qspi_get_name(struct spi_mem * spimem)
- Line: 976

### atmel_qspi_init
- Return type: static int
- Signature: atmel_qspi_init(struct atmel_qspi * aq)
- Line: 1262

### atmel_qspi_interrupt
- Return type: static irqreturn_t
- Signature: atmel_qspi_interrupt(int irq,void * dev_id)
- Line: 1287

### atmel_qspi_is_compatible
- Return type: static bool
- Signature: atmel_qspi_is_compatible(const struct spi_mem_op * op,const struct atmel_qspi_mode * mode)
- Line: 443

### atmel_qspi_probe
- Return type: static int
- Signature: atmel_qspi_probe(struct platform_device * pdev)
- Line: 1348

### atmel_qspi_read
- Return type: static u32
- Signature: atmel_qspi_read(struct atmel_qspi * aq,u32 offset)
- Line: 395

### atmel_qspi_reg_name
- Return type: static const char *
- Signature: atmel_qspi_reg_name(u32 offset,char * tmp,size_t sz)
- Line: 333

### atmel_qspi_reg_sync
- Return type: static int
- Signature: atmel_qspi_reg_sync(struct atmel_qspi * aq)
- Line: 421

### atmel_qspi_remove
- Return type: static void
- Signature: atmel_qspi_remove(struct platform_device * pdev)
- Line: 1502

### atmel_qspi_resume
- Return type: static int __maybe_unused
- Signature: atmel_qspi_resume(struct device * dev)
- Line: 1557

### atmel_qspi_runtime_resume
- Return type: static int __maybe_unused
- Signature: atmel_qspi_runtime_resume(struct device * dev)
- Line: 1600

### atmel_qspi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: atmel_qspi_runtime_suspend(struct device * dev)
- Line: 1589

### atmel_qspi_sama7g5_find_mode
- Return type: static int
- Signature: atmel_qspi_sama7g5_find_mode(const struct spi_mem_op * op)
- Line: 469

### atmel_qspi_sama7g5_init
- Return type: static int
- Signature: atmel_qspi_sama7g5_init(struct atmel_qspi * aq)
- Line: 1103

### atmel_qspi_sama7g5_set_cfg
- Return type: static int
- Signature: atmel_qspi_sama7g5_set_cfg(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
- Line: 688

### atmel_qspi_sama7g5_setup
- Return type: static int
- Signature: atmel_qspi_sama7g5_setup(struct spi_device * spi)
- Line: 1152

### atmel_qspi_sama7g5_suspend
- Return type: static int
- Signature: atmel_qspi_sama7g5_suspend(struct atmel_qspi * aq)
- Line: 1465

### atmel_qspi_sama7g5_transfer
- Return type: static int
- Signature: atmel_qspi_sama7g5_transfer(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
- Line: 882

### atmel_qspi_set_cfg
- Return type: static int
- Signature: atmel_qspi_set_cfg(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
- Line: 524

### atmel_qspi_set_cs_timing
- Return type: static int
- Signature: atmel_qspi_set_cs_timing(struct spi_device * spi)
- Line: 1201

### atmel_qspi_set_gclk
- Return type: static int
- Signature: atmel_qspi_set_gclk(struct atmel_qspi * aq)
- Line: 1062

### atmel_qspi_set_pad_calibration
- Return type: static int
- Signature: atmel_qspi_set_pad_calibration(struct atmel_qspi * aq)
- Line: 987

### atmel_qspi_set_serial_memory_mode
- Return type: static int
- Signature: atmel_qspi_set_serial_memory_mode(struct atmel_qspi * aq)
- Line: 509

### atmel_qspi_setup
- Return type: static int
- Signature: atmel_qspi_setup(struct spi_device * spi)
- Line: 1162

### atmel_qspi_supports_op
- Return type: static bool
- Signature: atmel_qspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 480

### atmel_qspi_suspend
- Return type: static int __maybe_unused
- Signature: atmel_qspi_suspend(struct device * dev)
- Line: 1530

### atmel_qspi_transfer
- Return type: static int
- Signature: atmel_qspi_transfer(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
- Line: 654

### atmel_qspi_update_config
- Return type: static int
- Signature: atmel_qspi_update_config(struct atmel_qspi * aq)
- Line: 432

### atmel_qspi_wait_for_completion
- Return type: static int
- Signature: atmel_qspi_wait_for_completion(struct atmel_qspi * aq,u32 irq_mask)
- Line: 631

### atmel_qspi_write
- Return type: static void
- Signature: atmel_qspi_write(u32 value,struct atmel_qspi * aq,u32 offset)
- Line: 409

## Structs (5)

### atmel_qspi
- Line: 273
- Members:
  - pclk_rate: u32
  - pclk_div: u8
  - max_speed_hz: u32
  - has_qspick: bool
  - has_gclk: bool
  - has_ricr: bool
  - octal: bool
  - has_dma: bool
  - has_2xgclk: bool
  - has_padcalib: bool
  - has_dllon: bool
  - regs: void __iomem *
  - mem: void __iomem *
  - pclk: clk *
  - qspick: clk *
  - gclk: clk *
  - pdev: platform_device *
  - caps: const struct atmel_qspi_caps *
  - ops: const struct atmel_qspi_ops *
  - mmap_size: resource_size_t
  - pending: u32
  - irq_mask: u32
  - mr: u32
  - scr: u32
  - target_max_speed_hz: u32
  - cmd_completion: completion
  - dma_completion: completion
  - mmap_phys_base: dma_addr_t
  - rx_chan: dma_chan *
  - tx_chan: dma_chan *
  - set_cfg: int (*)(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
  - transfer: int (*)(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
  - cmd_buswidth: u8
  - addr_buswidth: u8
  - data_buswidth: u8
  - config: u32

### atmel_qspi_caps
- Line: 259
- Members:
  - pclk_rate: u32
  - pclk_div: u8
  - max_speed_hz: u32
  - has_qspick: bool
  - has_gclk: bool
  - has_ricr: bool
  - octal: bool
  - has_dma: bool
  - has_2xgclk: bool
  - has_padcalib: bool
  - has_dllon: bool
  - regs: void __iomem *
  - mem: void __iomem *
  - pclk: clk *
  - qspick: clk *
  - gclk: clk *
  - pdev: platform_device *
  - caps: const struct atmel_qspi_caps *
  - ops: const struct atmel_qspi_ops *
  - mmap_size: resource_size_t
  - pending: u32
  - irq_mask: u32
  - mr: u32
  - scr: u32
  - target_max_speed_hz: u32
  - cmd_completion: completion
  - dma_completion: completion
  - mmap_phys_base: dma_addr_t
  - rx_chan: dma_chan *
  - tx_chan: dma_chan *
  - set_cfg: int (*)(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
  - transfer: int (*)(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
  - cmd_buswidth: u8
  - addr_buswidth: u8
  - data_buswidth: u8
  - config: u32

### atmel_qspi_mode
- Line: 302
- Members:
  - pclk_rate: u32
  - pclk_div: u8
  - max_speed_hz: u32
  - has_qspick: bool
  - has_gclk: bool
  - has_ricr: bool
  - octal: bool
  - has_dma: bool
  - has_2xgclk: bool
  - has_padcalib: bool
  - has_dllon: bool
  - regs: void __iomem *
  - mem: void __iomem *
  - pclk: clk *
  - qspick: clk *
  - gclk: clk *
  - pdev: platform_device *
  - caps: const struct atmel_qspi_caps *
  - ops: const struct atmel_qspi_ops *
  - mmap_size: resource_size_t
  - pending: u32
  - irq_mask: u32
  - mr: u32
  - scr: u32
  - target_max_speed_hz: u32
  - cmd_completion: completion
  - dma_completion: completion
  - mmap_phys_base: dma_addr_t
  - rx_chan: dma_chan *
  - tx_chan: dma_chan *
  - set_cfg: int (*)(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
  - transfer: int (*)(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
  - cmd_buswidth: u8
  - addr_buswidth: u8
  - data_buswidth: u8
  - config: u32

### atmel_qspi_ops
- Line: 295
- Members:
  - pclk_rate: u32
  - pclk_div: u8
  - max_speed_hz: u32
  - has_qspick: bool
  - has_gclk: bool
  - has_ricr: bool
  - octal: bool
  - has_dma: bool
  - has_2xgclk: bool
  - has_padcalib: bool
  - has_dllon: bool
  - regs: void __iomem *
  - mem: void __iomem *
  - pclk: clk *
  - qspick: clk *
  - gclk: clk *
  - pdev: platform_device *
  - caps: const struct atmel_qspi_caps *
  - ops: const struct atmel_qspi_ops *
  - mmap_size: resource_size_t
  - pending: u32
  - irq_mask: u32
  - mr: u32
  - scr: u32
  - target_max_speed_hz: u32
  - cmd_completion: completion
  - dma_completion: completion
  - mmap_phys_base: dma_addr_t
  - rx_chan: dma_chan *
  - tx_chan: dma_chan *
  - set_cfg: int (*)(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
  - transfer: int (*)(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
  - cmd_buswidth: u8
  - addr_buswidth: u8
  - data_buswidth: u8
  - config: u32

### atmel_qspi_pcal
- Line: 242
- Members:
  - pclk_rate: u32
  - pclk_div: u8
  - max_speed_hz: u32
  - has_qspick: bool
  - has_gclk: bool
  - has_ricr: bool
  - octal: bool
  - has_dma: bool
  - has_2xgclk: bool
  - has_padcalib: bool
  - has_dllon: bool
  - regs: void __iomem *
  - mem: void __iomem *
  - pclk: clk *
  - qspick: clk *
  - gclk: clk *
  - pdev: platform_device *
  - caps: const struct atmel_qspi_caps *
  - ops: const struct atmel_qspi_ops *
  - mmap_size: resource_size_t
  - pending: u32
  - irq_mask: u32
  - mr: u32
  - scr: u32
  - target_max_speed_hz: u32
  - cmd_completion: completion
  - dma_completion: completion
  - mmap_phys_base: dma_addr_t
  - rx_chan: dma_chan *
  - tx_chan: dma_chan *
  - set_cfg: int (*)(struct atmel_qspi * aq,const struct spi_mem_op * op,u32 * offset)
  - transfer: int (*)(struct spi_mem * mem,const struct spi_mem_op * op,u32 offset)
  - cmd_buswidth: u8
  - addr_buswidth: u8
  - data_buswidth: u8
  - config: u32

## Variables (16)

- static **atmel_qspi_driver** : platform_driver (line 1710)
- static **atmel_qspi_dt_ids** : const struct of_device_id[] (line 1674)
- static **atmel_qspi_mem_ops** : const struct spi_controller_mem_ops (line 981)
- static **atmel_qspi_modes** : const struct atmel_qspi_mode[] (line 309)
- static **atmel_qspi_ops** : const struct atmel_qspi_ops (line 1338)
- static **atmel_qspi_pm_ops** : const struct dev_pm_ops __maybe_unused (line 1617)
- static **atmel_qspi_sama7g5_modes** : const struct atmel_qspi_mode[] (line 319)
- static **atmel_qspi_sama7g5_ops** : const struct atmel_qspi_ops (line 1343)
- static **atmel_sam9x60_qspi_caps** : const struct atmel_qspi_caps (line 1625)
- static **atmel_sam9x7_ospi_caps** : const struct atmel_qspi_caps (line 1630)
- static **atmel_sama5d2_qspi_caps** : const struct atmel_qspi_caps (line 1623)
- static **atmel_sama7d65_ospi_caps** : const struct atmel_qspi_caps (line 1640)
- static **atmel_sama7d65_qspi_caps** : const struct atmel_qspi_caps (line 1650)
- static **atmel_sama7g5_ospi_caps** : const struct atmel_qspi_caps (line 1658)
- static **atmel_sama7g5_qspi_caps** : const struct atmel_qspi_caps (line 1667)
- static **pcal** : const struct atmel_qspi_pcal[] (line 248)

## Macros (161)

- **ATMEL_QSPI_DMA_MIN_BYTES** (line 235)
- **ATMEL_QSPI_PCAL_ARRAY_SIZE** (line 247)
- **ATMEL_QSPI_SYNC_TIMEOUT** (line 230)
- **ATMEL_QSPI_TIMEOUT** (line 229)
- **QSPI_CALIB_TIME** (line 232)
- **QSPI_CR** (line 32)
- **QSPI_CR_DLLOFF** (line 72)
- **QSPI_CR_DLLON** (line 71)
- **QSPI_CR_LASTXFER** (line 79)
- **QSPI_CR_QSPIDIS** (line 70)
- **QSPI_CR_QSPIEN** (line 69)
- **QSPI_CR_RTOUT** (line 78)
- **QSPI_CR_SRFRSH** (line 74)
- **QSPI_CR_STPCAL** (line 73)
- **QSPI_CR_STTFR** (line 77)
- **QSPI_CR_SWRST** (line 75)
- **QSPI_CR_UPDCFG** (line 76)
- **QSPI_DLLCFG** (line 54)
- **QSPI_DLLCFG_RANGE** (line 198)
- **QSPI_DLLCFG_THRESHOLD_FREQ** (line 231)
- **QSPI_IAR** (line 43)
- **QSPI_IAR_ADDR** (line 136)
- **QSPI_ICR** (line 44)
- **QSPI_ICR_INST**(inst) (line 140)
- **QSPI_ICR_INST_MASK** (line 139)
- **QSPI_ICR_INST_MASK_SAMA7G5** (line 141)
- **QSPI_ICR_OPT**(opt) (line 143)
- **QSPI_ICR_OPT_MASK** (line 142)
- **QSPI_IDR** (line 38)
- **QSPI_IER** (line 37)
- **QSPI_IFR** (line 46)
- **QSPI_IFR_ADDREN** (line 158)
- **QSPI_IFR_ADDRL** (line 166)
- **QSPI_IFR_ADDRL_SAMA7G5** (line 167)
- **QSPI_IFR_APBTFRTYP_READ** (line 176)
- **QSPI_IFR_CRM** (line 170)
- **QSPI_IFR_DATAEN** (line 160)
- **QSPI_IFR_DDRCMDEN** (line 178)
- **QSPI_IFR_DDREN** (line 171)
- **QSPI_IFR_DQSEN** (line 177)
- **QSPI_IFR_END** (line 174)
- **QSPI_IFR_HFWBEN** (line 179)
- **QSPI_IFR_INSTEN** (line 157)
- **QSPI_IFR_NBDUM**(n) (line 173)
- **QSPI_IFR_NBDUM_MASK** (line 172)
- **QSPI_IFR_OPTEN** (line 159)
- **QSPI_IFR_OPTL_1BIT** (line 162)
- **QSPI_IFR_OPTL_2BIT** (line 163)
- **QSPI_IFR_OPTL_4BIT** (line 164)
- **QSPI_IFR_OPTL_8BIT** (line 165)
- **QSPI_IFR_OPTL_MASK** (line 161)
- **QSPI_IFR_PROTTYP** (line 180)
- **QSPI_IFR_PROTTYP_HYPERFLASH** (line 184)
- **QSPI_IFR_PROTTYP_OCTAFLASH** (line 183)
- **QSPI_IFR_PROTTYP_STD_SPI** (line 181)
- **QSPI_IFR_PROTTYP_TWIN_QUAD** (line 182)
- **QSPI_IFR_SAMA5D2_WRITE_TRSFR** (line 169)
- **QSPI_IFR_SMRM** (line 175)
- **QSPI_IFR_TFRTYP_MEM** (line 168)
- **QSPI_IFR_WIDTH_DUAL_CMD** (line 152)
- **QSPI_IFR_WIDTH_DUAL_IO** (line 150)
- **QSPI_IFR_WIDTH_DUAL_OUTPUT** (line 148)
- **QSPI_IFR_WIDTH_MASK** (line 146)
- **QSPI_IFR_WIDTH_OCT_CMD** (line 156)
- **QSPI_IFR_WIDTH_OCT_IO** (line 155)
- **QSPI_IFR_WIDTH_OCT_OUTPUT** (line 154)
- **QSPI_IFR_WIDTH_QUAD_CMD** (line 153)
- **QSPI_IFR_WIDTH_QUAD_IO** (line 151)
- **QSPI_IFR_WIDTH_QUAD_OUTPUT** (line 149)
- **QSPI_IFR_WIDTH_SINGLE_BIT_SPI** (line 147)
- **QSPI_IMR** (line 39)
- **QSPI_MR** (line 33)
- **QSPI_MR_CSMODE_LASTXFER** (line 89)
- **QSPI_MR_CSMODE_MASK** (line 87)
- **QSPI_MR_CSMODE_NOT_RELOADED** (line 88)
- **QSPI_MR_CSMODE_SYSTEMATICALLY** (line 90)
- **QSPI_MR_DLYBCT**(n) (line 95)
- **QSPI_MR_DLYBCT_MASK** (line 94)
- **QSPI_MR_DLYCS**(n) (line 97)
- **QSPI_MR_DLYCS_MASK** (line 96)
- **QSPI_MR_DQSDLYEN** (line 86)
- **QSPI_MR_LLB** (line 83)
- **QSPI_MR_NBBITS**(n) (line 92)
- **QSPI_MR_NBBITS_MASK** (line 91)
- **QSPI_MR_OENSD** (line 93)
- **QSPI_MR_SMM** (line 82)
- **QSPI_MR_SMRM** (line 85)
- **QSPI_MR_WDRBT** (line 84)
- **QSPI_PCALBP** (line 56)
- **QSPI_PCALBP_BPEN** (line 210)
- **QSPI_PCALBP_CALNBP** (line 212)
- **QSPI_PCALBP_CALPBP** (line 211)
- **QSPI_PCALCFG** (line 55)
- **QSPI_PCALCFG_AAON** (line 201)
- **QSPI_PCALCFG_CALCNT** (line 205)
- **QSPI_PCALCFG_CALN** (line 207)
- **QSPI_PCALCFG_CALP** (line 206)
- **QSPI_PCALCFG_CLKDIV** (line 204)
- **QSPI_PCALCFG_DAPCAL** (line 202)
- **QSPI_PCALCFG_DIFFPM** (line 203)
- **QSPI_RD** (line 34)
- **QSPI_REFRESH** (line 52)
- **QSPI_REFRESH_DELAY_COUNTER** (line 192)
- **QSPI_RICR** (line 47)
- **QSPI_SCR** (line 40)
- **QSPI_SCR_CPHA** (line 120)
- **QSPI_SCR_CPOL** (line 119)
- **QSPI_SCR_DLYBS**(n) (line 124)
- **QSPI_SCR_DLYBS_MASK** (line 123)
- **QSPI_SCR_SCBR**(n) (line 122)
- **QSPI_SCR_SCBR_MASK** (line 121)
- **QSPI_SKR** (line 50)
- **QSPI_SMR** (line 49)
- **QSPI_SMR_RVDIS** (line 188)
- **QSPI_SMR_SCREN** (line 187)
- **QSPI_SMR_SCRKL** (line 189)
- **QSPI_SR** (line 36)
- **QSPI_SR2** (line 41)
- **QSPI_SR2_CALBSY** (line 133)
- **QSPI_SR2_CSS** (line 129)
- **QSPI_SR2_DLOCK** (line 132)
- **QSPI_SR2_HIDLE** (line 131)
- **QSPI_SR2_QSPIENS** (line 128)
- **QSPI_SR2_RBUSY** (line 130)
- **QSPI_SR2_SYNCBSY** (line 127)
- **QSPI_SR_CMD_COMPLETED** (line 116)
- **QSPI_SR_CSFA** (line 110)
- **QSPI_SR_CSR** (line 104)
- **QSPI_SR_CSRA** (line 111)
- **QSPI_SR_CSS** (line 105)
- **QSPI_SR_INSTRE** (line 106)
- **QSPI_SR_LWRA** (line 107)
- **QSPI_SR_OVRES** (line 103)
- **QSPI_SR_QITF** (line 108)
- **QSPI_SR_QITR** (line 109)
- **QSPI_SR_QSPIENS** (line 114)
- **QSPI_SR_RDRF** (line 100)
- **QSPI_SR_RFRSHD** (line 112)
- **QSPI_SR_TDRE** (line 101)
- **QSPI_SR_TOUT** (line 113)
- **QSPI_SR_TXEMPTY** (line 102)
- **QSPI_TD** (line 35)
- **QSPI_TOUT** (line 57)
- **QSPI_TOUT_TCNTM** (line 215)
- **QSPI_VERSION** (line 62)
- **QSPI_WICR** (line 45)
- **QSPI_WPMR** (line 59)
- **QSPI_WPMR_WPCREN** (line 220)
- **QSPI_WPMR_WPEN** (line 218)
- **QSPI_WPMR_WPITEN** (line 219)
- **QSPI_WPMR_WPKEY**(wpkey) (line 222)
- **QSPI_WPMR_WPKEY_MASK** (line 221)
- **QSPI_WPSR** (line 60)
- **QSPI_WPSR_WPVS** (line 225)
- **QSPI_WPSR_WPVSRC**(src) (line 227)
- **QSPI_WPSR_WPVSRC_MASK** (line 226)
- **QSPI_WRACNT** (line 53)
- **QSPI_WRACNT_NBWRA** (line 195)
- **SAM9X7_QSPI_MAX_SPEED_HZ** (line 66)
- **SAMA7G5_QSPI0_MAX_SPEED_HZ** (line 64)
- **SAMA7G5_QSPI1_SDR_MAX_SPEED_HZ** (line 65)
