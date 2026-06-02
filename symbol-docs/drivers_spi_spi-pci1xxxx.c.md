# drivers/spi/spi-pci1xxxx.c

Subsystem: drivers/spi

## Functions (28)

### pci1xxxx_acquire_sys_lock
- Return type: static int
- Signature: pci1xxxx_acquire_sys_lock(struct pci1xxxx_spi * par)
- Line: 210

### pci1xxxx_check_spi_can_dma
- Return type: static int
- Signature: pci1xxxx_check_spi_can_dma(struct pci1xxxx_spi * spi_bus,int hw_inst,int num_vector)
- Line: 224

### pci1xxxx_get_clock_div
- Return type: static u8
- Signature: pci1xxxx_get_clock_div(struct pci1xxxx_spi * par,u32 hz)
- Line: 385

### pci1xxxx_release_sys_lock
- Return type: static void
- Signature: pci1xxxx_release_sys_lock(struct pci1xxxx_spi * par)
- Line: 219

### pci1xxxx_set_sys_lock
- Return type: static int
- Signature: pci1xxxx_set_sys_lock(struct pci1xxxx_spi * par)
- Line: 204

### pci1xxxx_spi_can_dma
- Return type: static bool
- Signature: pci1xxxx_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 790

### pci1xxxx_spi_dma_config
- Return type: static void
- Signature: pci1xxxx_spi_dma_config(struct pci1xxxx_spi * spi_bus)
- Line: 277

### pci1xxxx_spi_dma_init
- Return type: static int
- Signature: pci1xxxx_spi_dma_init(struct pci1xxxx_spi * spi_bus,int hw_inst,int num_vector)
- Line: 325

### pci1xxxx_spi_isr
- Return type: static irqreturn_t
- Signature: pci1xxxx_spi_isr(int irq,void * dev)
- Line: 769

### pci1xxxx_spi_isr_dma
- Return type: static irqreturn_t
- Signature: pci1xxxx_spi_isr_dma(int irq,void * dev)
- Line: 752

### pci1xxxx_spi_isr_dma_rd
- Return type: static irqreturn_t
- Signature: pci1xxxx_spi_isr_dma_rd(int irq,void * dev)
- Line: 691

### pci1xxxx_spi_isr_dma_wr
- Return type: static irqreturn_t
- Signature: pci1xxxx_spi_isr_dma_wr(int irq,void * dev)
- Line: 719

### pci1xxxx_spi_isr_io
- Return type: static irqreturn_t
- Signature: pci1xxxx_spi_isr_io(int irq,void * dev)
- Line: 640

### pci1xxxx_spi_probe
- Return type: static int
- Signature: pci1xxxx_spi_probe(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 800

### pci1xxxx_spi_resume
- Return type: static int
- Signature: pci1xxxx_spi_resume(struct device * dev)
- Line: 971

### pci1xxxx_spi_set_cs
- Return type: static void
- Signature: pci1xxxx_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 367

### pci1xxxx_spi_setup
- Return type: static void
- Signature: pci1xxxx_spi_setup(struct pci1xxxx_spi * par,u8 hw_inst,u32 mode,u8 clkdiv,u32 len)
- Line: 450

### pci1xxxx_spi_setup_dma_from_io
- Return type: static void
- Signature: pci1xxxx_spi_setup_dma_from_io(struct pci1xxxx_spi_internal * p,dma_addr_t dma_addr,u32 len)
- Line: 430

### pci1xxxx_spi_setup_dma_to_io
- Return type: static void
- Signature: pci1xxxx_spi_setup_dma_to_io(struct pci1xxxx_spi_internal * p,dma_addr_t dma_addr,u32 len)
- Line: 409

### pci1xxxx_spi_setup_next_dma_from_io_transfer
- Return type: static void
- Signature: pci1xxxx_spi_setup_next_dma_from_io_transfer(struct pci1xxxx_spi_internal * p)
- Line: 679

### pci1xxxx_spi_setup_next_dma_to_io_transfer
- Return type: static void
- Signature: pci1xxxx_spi_setup_next_dma_to_io_transfer(struct pci1xxxx_spi_internal * p)
- Line: 661

### pci1xxxx_spi_shared_isr
- Return type: static irqreturn_t
- Signature: pci1xxxx_spi_shared_isr(int irq,void * dev)
- Line: 779

### pci1xxxx_spi_suspend
- Return type: static int
- Signature: pci1xxxx_spi_suspend(struct device * dev)
- Line: 991

### pci1xxxx_spi_transfer_one
- Return type: static int
- Signature: pci1xxxx_spi_transfer_one(struct spi_controller * spi_ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 631

### pci1xxxx_spi_transfer_with_dma
- Return type: static int
- Signature: pci1xxxx_spi_transfer_with_dma(struct spi_controller * spi_ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 538

### pci1xxxx_spi_transfer_with_io
- Return type: static int
- Signature: pci1xxxx_spi_transfer_with_io(struct spi_controller * spi_ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 477

### pci1xxxx_start_spi_xfer
- Return type: static void
- Signature: pci1xxxx_start_spi_xfer(struct pci1xxxx_spi_internal * p)
- Line: 467

### store_restore_config
- Return type: static void
- Signature: store_restore_config(struct pci1xxxx_spi * spi_ptr,struct pci1xxxx_spi_internal * spi_sub_ptr,u8 inst,bool store)
- Line: 945

## Structs (3)

### __anon75fe834f0108
- Line: 155
- Members:
  - hw_inst: u8
  - clkdiv: u8
  - irq: int[]
  - mode: int
  - spi_xfer_in_progress: bool
  - dma_completion_count: atomic_t
  - rx_buf: void *
  - dma_aborted_rd: bool
  - bytes_recvd: u32
  - tx_sgl_len: u32
  - rx_sgl_len: u32
  - rx_sgl: scatterlist *
  - tx_sgl: scatterlist *
  - dma_aborted_wr: bool
  - spi_xfer_done: completion
  - spi_host: spi_controller *
  - parent: pci1xxxx_spi *
  - xfer: spi_transfer *
  - dev_sel: unsigned int:3
  - msi_vector_sel: unsigned int:1
  - prev_val: pci1xxxx_spi_internal::__anon75fe834f0108
  - dev: pci_dev *
  - total_hw_instances: u8
  - dev_rev: u8
  - reg_base: void __iomem *
  - dma_offset_bar: void __iomem *
  - dma_rd_reg_lock: spinlock_t
  - dma_wr_reg_lock: spinlock_t
  - can_dma: bool

### pci1xxxx_spi
- Line: 161
- Members:
  - hw_inst: u8
  - clkdiv: u8
  - irq: int[]
  - mode: int
  - spi_xfer_in_progress: bool
  - dma_completion_count: atomic_t
  - rx_buf: void *
  - dma_aborted_rd: bool
  - bytes_recvd: u32
  - tx_sgl_len: u32
  - rx_sgl_len: u32
  - rx_sgl: scatterlist *
  - tx_sgl: scatterlist *
  - dma_aborted_wr: bool
  - spi_xfer_done: completion
  - spi_host: spi_controller *
  - parent: pci1xxxx_spi *
  - xfer: spi_transfer *
  - dev_sel: unsigned int:3
  - msi_vector_sel: unsigned int:1
  - prev_val: pci1xxxx_spi_internal::__anon75fe834f0108
  - dev: pci_dev *
  - total_hw_instances: u8
  - dev_rev: u8
  - reg_base: void __iomem *
  - dma_offset_bar: void __iomem *
  - dma_rd_reg_lock: spinlock_t
  - dma_wr_reg_lock: spinlock_t
  - can_dma: bool

### pci1xxxx_spi_internal
- Line: 137
- Members:
  - hw_inst: u8
  - clkdiv: u8
  - irq: int[]
  - mode: int
  - spi_xfer_in_progress: bool
  - dma_completion_count: atomic_t
  - rx_buf: void *
  - dma_aborted_rd: bool
  - bytes_recvd: u32
  - tx_sgl_len: u32
  - rx_sgl_len: u32
  - rx_sgl: scatterlist *
  - tx_sgl: scatterlist *
  - dma_aborted_wr: bool
  - spi_xfer_done: completion
  - spi_host: spi_controller *
  - parent: pci1xxxx_spi *
  - xfer: spi_transfer *
  - dev_sel: unsigned int:3
  - msi_vector_sel: unsigned int:1
  - prev_val: pci1xxxx_spi_internal::__anon75fe834f0108
  - dev: pci_dev *
  - total_hw_instances: u8
  - dev_rev: u8
  - reg_base: void __iomem *
  - dma_offset_bar: void __iomem *
  - dma_rd_reg_lock: spinlock_t
  - dma_wr_reg_lock: spinlock_t
  - can_dma: bool

## Variables (2)

- static **pci1xxxx_spi_driver** : pci_driver (line 1017)
- static **pci1xxxx_spi_pci_id_table** : const struct pci_device_id[] (line 175)

## Macros (92)

- **DEV_REV_MASK** (line 53)
- **DEV_REV_REG** (line 48)
- **DMA_CH_CONTROL_LIE** (line 102)
- **DMA_CH_CONTROL_RIE** (line 103)
- **DMA_INTR_EN** (line 104)
- **DRV_NAME** (line 21)
- **NUM_VEC_PER_INST** (line 135)
- **PCI1XXXX_IRQ_FLAGS** (line 118)
- **PCI1XXXX_SPI_BUFFER_SIZE** (line 33)
- **PCI1XXXX_SPI_CLK_10MHZ** (line 30)
- **PCI1XXXX_SPI_CLK_12MHZ** (line 29)
- **PCI1XXXX_SPI_CLK_15MHZ** (line 28)
- **PCI1XXXX_SPI_CLK_20MHZ** (line 27)
- **PCI1XXXX_SPI_CLK_25MHZ** (line 26)
- **PCI1XXXX_SPI_MAX_CLOCK_HZ** (line 25)
- **PCI1XXXX_SPI_MIN_CLOCK_HZ** (line 31)
- **PCI1XXXX_SPI_TIMEOUT** (line 121)
- **SPI0** (line 56)
- **SPI1** (line 57)
- **SPIALERT_MST_DB_REG_OFFSET**(x) (line 114)
- **SPIALERT_MST_VAL_REG_OFFSET**(x) (line 115)
- **SPI_CHIP_SEL_COUNT** (line 129)
- **SPI_CONFIG_PERI_ENABLE_REG** (line 50)
- **SPI_DMA_ABORT_INT_MASK**(x) (line 101)
- **SPI_DMA_ADDR_BASE** (line 60)
- **SPI_DMA_CH0_ABORT_INT** (line 98)
- **SPI_DMA_CH0_DONE_INT** (line 96)
- **SPI_DMA_CH0_RD_BASE** (line 85)
- **SPI_DMA_CH0_WR_BASE** (line 84)
- **SPI_DMA_CH1_ABORT_INT** (line 99)
- **SPI_DMA_CH1_DONE_INT** (line 97)
- **SPI_DMA_CH1_RD_BASE** (line 87)
- **SPI_DMA_CH1_WR_BASE** (line 86)
- **SPI_DMA_CH_CTL1_OFFSET** (line 89)
- **SPI_DMA_CH_DAR_HI_OFFSET** (line 94)
- **SPI_DMA_CH_DAR_LO_OFFSET** (line 93)
- **SPI_DMA_CH_SAR_HI_OFFSET** (line 92)
- **SPI_DMA_CH_SAR_LO_OFFSET** (line 91)
- **SPI_DMA_CH_XFER_LEN_OFFSET** (line 90)
- **SPI_DMA_DONE_INT_MASK**(x) (line 100)
- **SPI_DMA_ENGINE_DIS** (line 124)
- **SPI_DMA_ENGINE_EN** (line 123)
- **SPI_DMA_ERR_RD_STS** (line 77)
- **SPI_DMA_ERR_WR_STS** (line 68)
- **SPI_DMA_GLOBAL_RD_ENGINE_EN** (line 63)
- **SPI_DMA_GLOBAL_WR_ENGINE_EN** (line 61)
- **SPI_DMA_INTR_IMWR_RABORT_HIGH** (line 81)
- **SPI_DMA_INTR_IMWR_RABORT_LOW** (line 80)
- **SPI_DMA_INTR_IMWR_RDONE_HIGH** (line 79)
- **SPI_DMA_INTR_IMWR_RDONE_LOW** (line 78)
- **SPI_DMA_INTR_IMWR_WABORT_HIGH** (line 72)
- **SPI_DMA_INTR_IMWR_WABORT_LOW** (line 71)
- **SPI_DMA_INTR_IMWR_WDONE_HIGH** (line 70)
- **SPI_DMA_INTR_IMWR_WDONE_LOW** (line 69)
- **SPI_DMA_INTR_RD_CLR** (line 76)
- **SPI_DMA_INTR_RD_IMWR_DATA** (line 82)
- **SPI_DMA_INTR_RD_STS** (line 74)
- **SPI_DMA_INTR_WR_CLR** (line 67)
- **SPI_DMA_INTR_WR_IMWR_DATA** (line 73)
- **SPI_DMA_INTR_WR_STS** (line 65)
- **SPI_DMA_RD_DOORBELL_REG** (line 64)
- **SPI_DMA_RD_INT_MASK** (line 75)
- **SPI_DMA_WR_DOORBELL_REG** (line 62)
- **SPI_DMA_WR_INT_MASK** (line 66)
- **SPI_FORCE_CE** (line 127)
- **SPI_INTR** (line 126)
- **SPI_MAX_DATA_LEN** (line 119)
- **SPI_MSI_VECTOR_SEL_MASK** (line 38)
- **SPI_MST1_ADDR_BASE** (line 46)
- **SPI_MST_CMD_BUF_OFFSET**(x) (line 108)
- **SPI_MST_CTL_CMD_LEN_MASK** (line 36)
- **SPI_MST_CTL_DEVSEL_MASK** (line 35)
- **SPI_MST_CTL_FORCE_CE** (line 40)
- **SPI_MST_CTL_GO** (line 42)
- **SPI_MST_CTL_MODE_SEL** (line 41)
- **SPI_MST_CTL_REG_OFFSET**(x) (line 110)
- **SPI_MST_CTL_SPEED_MASK** (line 37)
- **SPI_MST_EVENT_MASK_REG_OFFSET**(x) (line 112)
- **SPI_MST_EVENT_REG_OFFSET**(x) (line 111)
- **SPI_MST_PAD_CTL_REG_OFFSET**(x) (line 113)
- **SPI_MST_RSP_BUF_OFFSET**(x) (line 109)
- **SPI_PCI_CTRL_REG_OFFSET**(x) (line 116)
- **SPI_PERI_ADDR_BASE** (line 44)
- **SPI_PERI_ENBLE_PF_MASK** (line 52)
- **SPI_RESUME_CONFIG** (line 133)
- **SPI_SUSPEND_CONFIG** (line 132)
- **SPI_SYSLOCK** (line 55)
- **SPI_SYSLOCK_REG** (line 49)
- **SPI_SYSTEM_ADDR_BASE** (line 45)
- **SYSLOCK_RETRY_CNT** (line 122)
- **SYS_FREQ_DEFAULT** (line 23)
- **VENDOR_ID_MCHP** (line 130)
