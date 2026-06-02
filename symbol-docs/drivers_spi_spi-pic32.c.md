# drivers/spi/spi-pic32.c

Subsystem: drivers/spi

## Functions (29)

### pic32_err_stop
- Return type: static void
- Signature: pic32_err_stop(struct pic32_spi * pic32s,const char * msg)
- Line: 219

### pic32_rx_fifo_level
- Return type: static u32
- Signature: pic32_rx_fifo_level(struct pic32_spi * pic32s)
- Line: 146

### pic32_rx_max
- Return type: static u32
- Signature: pic32_rx_max(struct pic32_spi * pic32s,int n_bytes)
- Line: 182

### pic32_spi_can_dma
- Return type: static bool
- Signature: pic32_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 484

### pic32_spi_cleanup
- Return type: static void
- Signature: pic32_spi_cleanup(struct spi_device * spi)
- Line: 600

### pic32_spi_disable
- Return type: static void
- Signature: pic32_spi_disable(struct pic32_spi * pic32s)
- Line: 128

### pic32_spi_dma_config
- Return type: static int
- Signature: pic32_spi_dma_config(struct pic32_spi * pic32s,u32 dma_width)
- Line: 357

### pic32_spi_dma_prep
- Return type: static int
- Signature: pic32_spi_dma_prep(struct pic32_spi * pic32s,struct device * dev)
- Line: 606

### pic32_spi_dma_rx_notify
- Return type: static void
- Signature: pic32_spi_dma_rx_notify(void * data)
- Line: 293

### pic32_spi_dma_transfer
- Return type: static int
- Signature: pic32_spi_dma_transfer(struct pic32_spi * pic32s,struct spi_transfer * xfer)
- Line: 300

### pic32_spi_dma_unprep
- Return type: static void
- Signature: pic32_spi_dma_unprep(struct pic32_spi * pic32s)
- Line: 655

### pic32_spi_enable
- Return type: static void
- Signature: pic32_spi_enable(struct pic32_spi * pic32s)
- Line: 123

### pic32_spi_fault_irq
- Return type: static irqreturn_t
- Signature: pic32_spi_fault_irq(int irq,void * dev_id)
- Line: 233

### pic32_spi_hw_init
- Return type: static void
- Signature: pic32_spi_hw_init(struct pic32_spi * pic32s)
- Line: 668

### pic32_spi_hw_probe
- Return type: static int
- Signature: pic32_spi_hw_probe(struct platform_device * pdev,struct pic32_spi * pic32s)
- Line: 707

### pic32_spi_one_transfer
- Return type: static int
- Signature: pic32_spi_one_transfer(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 495

### pic32_spi_prepare_hardware
- Return type: static int
- Signature: pic32_spi_prepare_hardware(struct spi_controller * host)
- Line: 433

### pic32_spi_prepare_message
- Return type: static int
- Signature: pic32_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 442

### pic32_spi_probe
- Return type: static int
- Signature: pic32_spi_probe(struct platform_device * pdev)
- Line: 749

### pic32_spi_remove
- Return type: static void
- Signature: pic32_spi_remove(struct platform_device * pdev)
- Line: 841

### pic32_spi_rx_irq
- Return type: static irqreturn_t
- Signature: pic32_spi_rx_irq(int irq,void * dev_id)
- Line: 261

### pic32_spi_set_clk_rate
- Return type: static void
- Signature: pic32_spi_set_clk_rate(struct pic32_spi * pic32s,u32 spi_ck)
- Line: 136

### pic32_spi_set_word_size
- Return type: static int
- Signature: pic32_spi_set_word_size(struct pic32_spi * pic32s,u8 bits_per_word)
- Line: 388

### pic32_spi_setup
- Return type: static int
- Signature: pic32_spi_setup(struct spi_device * spi)
- Line: 580

### pic32_spi_tx_irq
- Return type: static irqreturn_t
- Signature: pic32_spi_tx_irq(int irq,void * dev_id)
- Line: 280

### pic32_spi_unprepare_hardware
- Return type: static int
- Signature: pic32_spi_unprepare_hardware(struct spi_controller * host)
- Line: 570

### pic32_spi_unprepare_message
- Return type: static int
- Signature: pic32_spi_unprepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 563

### pic32_tx_fifo_level
- Return type: static u32
- Signature: pic32_tx_fifo_level(struct pic32_spi * pic32s)
- Line: 153

### pic32_tx_max
- Return type: static u32
- Signature: pic32_tx_max(struct pic32_spi * pic32s,int n_bytes)
- Line: 161

## Structs (2)

### pic32_spi
- Line: 95
- Members:
  - ctrl: u32
  - ctrl_clr: u32
  - ctrl_set: u32
  - ctrl_inv: u32
  - status: u32
  - status_clr: u32
  - status_set: u32
  - status_inv: u32
  - buf: u32
  - dontuse: u32[3]
  - baud: u32
  - dontuse2: u32[3]
  - ctrl2: u32
  - ctrl2_clr: u32
  - ctrl2_set: u32
  - ctrl2_inv: u32
  - dma_base: dma_addr_t
  - regs: pic32_spi_regs __iomem *
  - fault_irq: int
  - rx_irq: int
  - tx_irq: int
  - fifo_n_byte: u32
  - clk: clk *
  - host: spi_controller *
  - speed_hz: u32
  - mode: u32
  - bits_per_word: u32
  - fifo_n_elm: u32
  - flags: unsigned long
  - xfer_done: completion
  - tx: const void *
  - tx_end: const void *
  - rx: const void *
  - rx_end: const void *
  - len: int
  - rx_fifo: void (*)(struct pic32_spi *)
  - tx_fifo: void (*)(struct pic32_spi *)

### pic32_spi_regs
- Line: 26
- Members:
  - ctrl: u32
  - ctrl_clr: u32
  - ctrl_set: u32
  - ctrl_inv: u32
  - status: u32
  - status_clr: u32
  - status_set: u32
  - status_inv: u32
  - buf: u32
  - dontuse: u32[3]
  - baud: u32
  - dontuse2: u32[3]
  - ctrl2: u32
  - ctrl2_clr: u32
  - ctrl2_set: u32
  - ctrl2_inv: u32
  - dma_base: dma_addr_t
  - regs: pic32_spi_regs __iomem *
  - fault_irq: int
  - rx_irq: int
  - tx_irq: int
  - fifo_n_byte: u32
  - clk: clk *
  - host: spi_controller *
  - speed_hz: u32
  - mode: u32
  - bits_per_word: u32
  - fifo_n_elm: u32
  - flags: unsigned long
  - xfer_done: completion
  - tx: const void *
  - tx_end: const void *
  - rx: const void *
  - rx_end: const void *
  - len: int
  - rx_fifo: void (*)(struct pic32_spi *)
  - tx_fifo: void (*)(struct pic32_spi *)

## Variables (2)

- static **pic32_spi_driver** : platform_driver (line 861)
- static **pic32_spi_of_match** : const struct of_device_id[] (line 855)

## Macros (40)

- **BAUD_MASK** (line 85)
- **BUILD_SPI_FIFO_RW**(__name,__type,__bwl) (line 189)
- **CTRL2_FRM_ERR_EN** (line 90)
- **CTRL2_RX_OV_EN** (line 89)
- **CTRL2_TX_UR_EN** (line 88)
- **CTRL_BPW_MASK** (line 62)
- **CTRL_BPW_SHIFT** (line 63)
- **CTRL_CKE** (line 60)
- **CTRL_CKP** (line 59)
- **CTRL_ENHBUF** (line 69)
- **CTRL_FRMEN** (line 72)
- **CTRL_MCLKSEL** (line 70)
- **CTRL_MSSEN** (line 71)
- **CTRL_MSTEN** (line 58)
- **CTRL_ON** (line 68)
- **CTRL_RX_INT_SHIFT** (line 46)
- **CTRL_SIDL** (line 67)
- **CTRL_SMP** (line 61)
- **CTRL_TX_INT_SHIFT** (line 52)
- **PIC32F_DMA_PREP** (line 109)
- **PIC32_BPW_16** (line 65)
- **PIC32_BPW_32** (line 66)
- **PIC32_BPW_8** (line 64)
- **PIC32_DMA_LEN_MIN** (line 93)
- **RX_FIFO_EMPTY** (line 47)
- **RX_FIFO_FULL** (line 50)
- **RX_FIFO_HALF_FULL** (line 49)
- **RX_FIFO_NOT_EMPTY** (line 48)
- **STAT_FRM_ERR** (line 78)
- **STAT_RF_EMPTY** (line 75)
- **STAT_RF_LVL_MASK** (line 81)
- **STAT_RF_LVL_SHIFT** (line 82)
- **STAT_RX_OV** (line 76)
- **STAT_TF_LVL_MASK** (line 79)
- **STAT_TF_LVL_SHIFT** (line 80)
- **STAT_TX_UR** (line 77)
- **TX_FIFO_ALL_EMPTY** (line 53)
- **TX_FIFO_EMPTY** (line 54)
- **TX_FIFO_HALF_EMPTY** (line 55)
- **TX_FIFO_NOT_FULL** (line 56)
