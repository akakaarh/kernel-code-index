# drivers/spi/spi-topcliff-pch.c

Subsystem: drivers/spi

## Functions (39)

### pch_alloc_dma_buf
- Return type: static int
- Signature: pch_alloc_dma_buf(struct pch_spi_board_data * board_dat,struct pch_spi_data * data)
- Line: 1274

### pch_dma_rx_complete
- Return type: static void
- Signature: pch_dma_rx_complete(void * arg)
- Line: 797

### pch_free_dma_buf
- Return type: static void
- Signature: pch_free_dma_buf(struct pch_spi_board_data * board_dat,struct pch_spi_data * data)
- Line: 1260

### pch_spi_clear_fifo
- Return type: static void
- Signature: pch_spi_clear_fifo(struct spi_controller * host)
- Line: 257

### pch_spi_copy_rx_data
- Return type: static void
- Signature: pch_spi_copy_rx_data(struct pch_spi_data * data,int bpw)
- Line: 694

### pch_spi_copy_rx_data_for_dma
- Return type: static void
- Signature: pch_spi_copy_rx_data_for_dma(struct pch_spi_data * data,int bpw)
- Line: 715

### pch_spi_exit
- Return type: static void __exit
- Signature: pch_spi_exit(void)
- Line: 1673

### pch_spi_filter
- Return type: static bool
- Signature: pch_spi_filter(struct dma_chan * chan,void * slave)
- Line: 806

### pch_spi_free_resources
- Return type: static void
- Signature: pch_spi_free_resources(struct pch_spi_board_data * board_dat,struct pch_spi_data * data)
- Line: 1237

### pch_spi_get_resources
- Return type: static int
- Signature: pch_spi_get_resources(struct pch_spi_board_data * board_dat,struct pch_spi_data * data)
- Line: 1245

### pch_spi_handle_dma
- Return type: static void
- Signature: pch_spi_handle_dma(struct pch_spi_data * data,int * bpw)
- Line: 895

### pch_spi_handler
- Return type: static irqreturn_t
- Signature: pch_spi_handler(int irq,void * dev_id)
- Line: 337

### pch_spi_handler_sub
- Return type: static void
- Signature: pch_spi_handler_sub(struct pch_spi_data * data,u32 reg_spsr_val,void __iomem * io_remap_addr)
- Line: 263

### pch_spi_init
- Return type: static int __init
- Signature: pch_spi_init(void)
- Line: 1656

### pch_spi_nomore_transfer
- Return type: static void
- Signature: pch_spi_nomore_transfer(struct pch_spi_data * data)
- Line: 609

### pch_spi_pd_probe
- Return type: static int
- Signature: pch_spi_pd_probe(struct platform_device * plat_dev)
- Line: 1297

### pch_spi_pd_remove
- Return type: static void
- Signature: pch_spi_pd_remove(struct platform_device * plat_dev)
- Line: 1399

### pch_spi_pd_resume
- Return type: static int
- Signature: pch_spi_pd_resume(struct platform_device * pd_dev)
- Line: 1483

### pch_spi_pd_suspend
- Return type: static int
- Signature: pch_spi_pd_suspend(struct platform_device * pd_dev,pm_message_t state)
- Line: 1444

### pch_spi_probe
- Return type: static int
- Signature: pch_spi_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 1527

### pch_spi_process_messages
- Return type: static void
- Signature: pch_spi_process_messages(struct work_struct * pwork)
- Line: 1103

### pch_spi_readreg
- Return type: static u32
- Signature: pch_spi_readreg(struct spi_controller * host,int idx)
- Line: 234

### pch_spi_release_dma
- Return type: static void
- Signature: pch_spi_release_dma(struct pch_spi_data * data)
- Line: 878

### pch_spi_remove
- Return type: static void
- Signature: pch_spi_remove(struct pci_dev * pdev)
- Line: 1607

### pch_spi_request_dma
- Return type: static void
- Signature: pch_spi_request_dma(struct pch_spi_data * data,int bpw)
- Line: 819

### pch_spi_reset
- Return type: static void
- Signature: pch_spi_reset(struct spi_controller * host)
- Line: 447

### pch_spi_resume
- Return type: static int __maybe_unused
- Signature: pch_spi_resume(struct device * dev)
- Line: 1634

### pch_spi_select_chip
- Return type: static void
- Signature: pch_spi_select_chip(struct pch_spi_data * data,struct spi_device * pspi)
- Line: 498

### pch_spi_set_baud_rate
- Return type: static void
- Signature: pch_spi_set_baud_rate(struct spi_controller * host,u32 speed_hz)
- Line: 389

### pch_spi_set_bits_per_word
- Return type: static void
- Signature: pch_spi_set_bits_per_word(struct spi_controller * host,u8 bits_per_word)
- Line: 405

### pch_spi_set_host_mode
- Return type: static void
- Signature: pch_spi_set_host_mode(struct spi_controller * host)
- Line: 248

### pch_spi_set_ir
- Return type: static void
- Signature: pch_spi_set_ir(struct pch_spi_data * data)
- Line: 660

### pch_spi_set_tx
- Return type: static void
- Signature: pch_spi_set_tx(struct pch_spi_data * data,int * bpw)
- Line: 516

### pch_spi_setclr_reg
- Return type: static void
- Signature: pch_spi_setclr_reg(struct spi_controller * host,int idx,u32 set,u32 clr)
- Line: 240

### pch_spi_setup_transfer
- Return type: static void
- Signature: pch_spi_setup_transfer(struct spi_device * spi)
- Line: 418

### pch_spi_start_transfer
- Return type: static int
- Signature: pch_spi_start_transfer(struct pch_spi_data * data)
- Line: 742

### pch_spi_suspend
- Return type: static int __maybe_unused
- Signature: pch_spi_suspend(struct device * dev)
- Line: 1623

### pch_spi_transfer
- Return type: static int
- Signature: pch_spi_transfer(struct spi_device * pspi,struct spi_message * pmsg)
- Line: 456

### pch_spi_writereg
- Return type: static void
- Signature: pch_spi_writereg(struct spi_controller * host,int idx,u32 val)
- Line: 223

## Structs (4)

### pch_pd_dev_save
- Line: 203
- Members:
  - dma_dev: pci_dev *
  - desc_tx: dma_async_tx_descriptor *
  - desc_rx: dma_async_tx_descriptor *
  - param_tx: pch_dma_slave
  - param_rx: pch_dma_slave
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - sg_tx_p: scatterlist *
  - sg_rx_p: scatterlist *
  - sg_tx: scatterlist
  - sg_rx: scatterlist
  - nent: int
  - tx_buf_virt: void *
  - rx_buf_virt: void *
  - tx_buf_dma: dma_addr_t
  - rx_buf_dma: dma_addr_t
  - io_remap_addr: void __iomem *
  - io_base_addr: unsigned long
  - host: spi_controller *
  - work: work_struct
  - wait: wait_queue_head_t
  - transfer_complete: u8
  - bcurrent_msg_processing: u8
  - lock: spinlock_t
  - queue: list_head
  - status: u8
  - bpw_len: u32
  - transfer_active: u8
  - tx_index: u32
  - rx_index: u32
  - pkt_tx_buff: u16 *
  - pkt_rx_buff: u16 *
  - n_curnt_chip: u8
  - current_chip: spi_device *
  - current_msg: spi_message *
  - cur_trans: spi_transfer *
  - board_dat: pch_spi_board_data *
  - plat_dev: platform_device *
  - ch: int
  - dma: pch_spi_dma_ctrl
  - use_dma: int
  - irq_reg_sts: u8
  - save_total_len: int
  - pdev: pci_dev *
  - suspend_sts: u8
  - num: int
  - num: int
  - pd_save: platform_device * []
  - board_dat: pch_spi_board_data *

### pch_spi_board_data
- Line: 197
- Members:
  - dma_dev: pci_dev *
  - desc_tx: dma_async_tx_descriptor *
  - desc_rx: dma_async_tx_descriptor *
  - param_tx: pch_dma_slave
  - param_rx: pch_dma_slave
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - sg_tx_p: scatterlist *
  - sg_rx_p: scatterlist *
  - sg_tx: scatterlist
  - sg_rx: scatterlist
  - nent: int
  - tx_buf_virt: void *
  - rx_buf_virt: void *
  - tx_buf_dma: dma_addr_t
  - rx_buf_dma: dma_addr_t
  - io_remap_addr: void __iomem *
  - io_base_addr: unsigned long
  - host: spi_controller *
  - work: work_struct
  - wait: wait_queue_head_t
  - transfer_complete: u8
  - bcurrent_msg_processing: u8
  - lock: spinlock_t
  - queue: list_head
  - status: u8
  - bpw_len: u32
  - transfer_active: u8
  - tx_index: u32
  - rx_index: u32
  - pkt_tx_buff: u16 *
  - pkt_rx_buff: u16 *
  - n_curnt_chip: u8
  - current_chip: spi_device *
  - current_msg: spi_message *
  - cur_trans: spi_transfer *
  - board_dat: pch_spi_board_data *
  - plat_dev: platform_device *
  - ch: int
  - dma: pch_spi_dma_ctrl
  - use_dma: int
  - irq_reg_sts: u8
  - save_total_len: int
  - pdev: pci_dev *
  - suspend_sts: u8
  - num: int
  - num: int
  - pd_save: platform_device * []
  - board_dat: pch_spi_board_data *

### pch_spi_data
- Line: 161
- Members:
  - dma_dev: pci_dev *
  - desc_tx: dma_async_tx_descriptor *
  - desc_rx: dma_async_tx_descriptor *
  - param_tx: pch_dma_slave
  - param_rx: pch_dma_slave
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - sg_tx_p: scatterlist *
  - sg_rx_p: scatterlist *
  - sg_tx: scatterlist
  - sg_rx: scatterlist
  - nent: int
  - tx_buf_virt: void *
  - rx_buf_virt: void *
  - tx_buf_dma: dma_addr_t
  - rx_buf_dma: dma_addr_t
  - io_remap_addr: void __iomem *
  - io_base_addr: unsigned long
  - host: spi_controller *
  - work: work_struct
  - wait: wait_queue_head_t
  - transfer_complete: u8
  - bcurrent_msg_processing: u8
  - lock: spinlock_t
  - queue: list_head
  - status: u8
  - bpw_len: u32
  - transfer_active: u8
  - tx_index: u32
  - rx_index: u32
  - pkt_tx_buff: u16 *
  - pkt_rx_buff: u16 *
  - n_curnt_chip: u8
  - current_chip: spi_device *
  - current_msg: spi_message *
  - cur_trans: spi_transfer *
  - board_dat: pch_spi_board_data *
  - plat_dev: platform_device *
  - ch: int
  - dma: pch_spi_dma_ctrl
  - use_dma: int
  - irq_reg_sts: u8
  - save_total_len: int
  - pdev: pci_dev *
  - suspend_sts: u8
  - num: int
  - num: int
  - pd_save: platform_device * []
  - board_dat: pch_spi_board_data *

### pch_spi_dma_ctrl
- Line: 105
- Members:
  - dma_dev: pci_dev *
  - desc_tx: dma_async_tx_descriptor *
  - desc_rx: dma_async_tx_descriptor *
  - param_tx: pch_dma_slave
  - param_rx: pch_dma_slave
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - sg_tx_p: scatterlist *
  - sg_rx_p: scatterlist *
  - sg_tx: scatterlist
  - sg_rx: scatterlist
  - nent: int
  - tx_buf_virt: void *
  - rx_buf_virt: void *
  - tx_buf_dma: dma_addr_t
  - rx_buf_dma: dma_addr_t
  - io_remap_addr: void __iomem *
  - io_base_addr: unsigned long
  - host: spi_controller *
  - work: work_struct
  - wait: wait_queue_head_t
  - transfer_complete: u8
  - bcurrent_msg_processing: u8
  - lock: spinlock_t
  - queue: list_head
  - status: u8
  - bpw_len: u32
  - transfer_active: u8
  - tx_index: u32
  - rx_index: u32
  - pkt_tx_buff: u16 *
  - pkt_rx_buff: u16 *
  - n_curnt_chip: u8
  - current_chip: spi_device *
  - current_msg: spi_message *
  - cur_trans: spi_transfer *
  - board_dat: pch_spi_board_data *
  - plat_dev: platform_device *
  - ch: int
  - dma: pch_spi_dma_ctrl
  - use_dma: int
  - irq_reg_sts: u8
  - save_total_len: int
  - pdev: pci_dev *
  - suspend_sts: u8
  - num: int
  - num: int
  - pd_save: platform_device * []
  - board_dat: pch_spi_board_data *

## Variables (4)

- static **pch_spi_pcidev_driver** : pci_driver (line 1648)
- static **pch_spi_pcidev_id** : const struct pci_device_id[] (line 209)
- static **pch_spi_pd_driver** : platform_driver (line 1517)
- static **use_dma** : int (line 103)

## Macros (57)

- **MASK_RFIC_SPCR_BITS** (line 80)
- **MASK_SPBRR_SPBR_BITS** (line 79)
- **MASK_TFIC_SPCR_BITS** (line 81)
- **PCH_ADDRESS_SIZE** (line 30)
- **PCH_ALL** (line 73)
- **PCH_BUF_SIZE** (line 100)
- **PCH_CLOCK_HZ** (line 83)
- **PCH_DMA_TRANS_SIZE** (line 101)
- **PCH_MAX_BAUDRATE** (line 43)
- **PCH_MAX_CS** (line 53)
- **PCH_MAX_FIFO_DEPTH** (line 44)
- **PCH_MAX_SPBR** (line 84)
- **PCH_READABLE**(x) (line 35)
- **PCH_RX_THOLD** (line 38)
- **PCH_RX_THOLD_MAX** (line 39)
- **PCH_SLEEP_TIME** (line 48)
- **PCH_SPBRR** (line 24)
- **PCH_SPCR** (line 23)
- **PCH_SPDRR** (line 27)
- **PCH_SPDWR** (line 26)
- **PCH_SPI_MAX_DEV** (line 98)
- **PCH_SPSR** (line 25)
- **PCH_SPSR_RFD** (line 33)
- **PCH_SPSR_TFD** (line 32)
- **PCH_SRST** (line 29)
- **PCH_SSNXCR** (line 28)
- **PCH_TX_THOLD** (line 41)
- **PCH_WRITABLE**(x) (line 36)
- **PCI_DEVICE_ID_GE_SPI** (line 54)
- **PCI_DEVICE_ID_ML7213_SPI** (line 87)
- **PCI_DEVICE_ID_ML7223_SPI** (line 88)
- **PCI_DEVICE_ID_ML7831_SPI** (line 89)
- **SPBRR_SIZE_BIT** (line 71)
- **SPCR_CPHA_BIT** (line 59)
- **SPCR_CPOL_BIT** (line 60)
- **SPCR_FICLR_BIT** (line 66)
- **SPCR_FIE_BIT** (line 63)
- **SPCR_LSBF_BIT** (line 58)
- **SPCR_MDFIE_BIT** (line 65)
- **SPCR_MSTR_BIT** (line 57)
- **SPCR_ORIE_BIT** (line 64)
- **SPCR_RFIC_FIELD** (line 76)
- **SPCR_RFIE_BIT** (line 62)
- **SPCR_SPE_BIT** (line 56)
- **SPCR_TFIC_FIELD** (line 77)
- **SPCR_TFIE_BIT** (line 61)
- **SPSR_FI_BIT** (line 69)
- **SPSR_ORF_BIT** (line 70)
- **SPSR_RFI_BIT** (line 68)
- **SPSR_TFI_BIT** (line 67)
- **SSN_HIGH** (line 51)
- **SSN_LOW** (line 50)
- **SSN_NO_CONTROL** (line 52)
- **STATUS_EXITING** (line 47)
- **STATUS_RUNNING** (line 46)
- **pch_spi_pd_resume** (line 1514)
- **pch_spi_pd_suspend** (line 1513)
