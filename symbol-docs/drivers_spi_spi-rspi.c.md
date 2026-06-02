# drivers/spi/spi-rspi.c

Subsystem: drivers/spi

## Functions (57)

### __rspi_can_dma
- Return type: static bool
- Signature: __rspi_can_dma(const struct rspi_data * rspi,const struct spi_transfer * xfer)
- Line: 680

### qspi_receive_init
- Return type: static void
- Signature: qspi_receive_init(const struct rspi_data * rspi)
- Line: 669

### qspi_set_config_register
- Return type: static int
- Signature: qspi_set_config_register(struct rspi_data * rspi,int access_size)
- Line: 338

### qspi_set_receive_trigger
- Return type: static int
- Signature: qspi_set_receive_trigger(struct rspi_data * rspi,unsigned int len)
- Line: 430

### qspi_set_send_trigger
- Return type: static unsigned int
- Signature: qspi_set_send_trigger(struct rspi_data * rspi,unsigned int len)
- Line: 410

### qspi_setup_sequencer
- Return type: static int
- Signature: qspi_setup_sequencer(struct rspi_data * rspi,const struct spi_message * msg)
- Line: 906

### qspi_transfer_in
- Return type: static int
- Signature: qspi_transfer_in(struct rspi_data * rspi,struct spi_transfer * xfer)
- Line: 833

### qspi_transfer_mode
- Return type: static u16
- Signature: qspi_transfer_mode(const struct spi_transfer * xfer)
- Line: 882

### qspi_transfer_one
- Return type: static int
- Signature: qspi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 862

### qspi_transfer_out
- Return type: static int
- Signature: qspi_transfer_out(struct rspi_data * rspi,struct spi_transfer * xfer)
- Line: 801

### qspi_transfer_out_in
- Return type: static int
- Signature: qspi_transfer_out_in(struct rspi_data * rspi,struct spi_transfer * xfer)
- Line: 786

### qspi_trigger_transfer_out_in
- Return type: static int
- Signature: qspi_trigger_transfer_out_in(struct rspi_data * rspi,const u8 * tx,u8 * rx,unsigned int len)
- Line: 755

### qspi_update
- Return type: static void
- Signature: qspi_update(const struct rspi_data * rspi,u8 mask,u8 val,u8 reg)
- Line: 400

### rspi_can_dma
- Return type: static bool
- Signature: rspi_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 686

### rspi_common_transfer
- Return type: static int
- Signature: rspi_common_transfer(struct rspi_data * rspi,struct spi_transfer * xfer)
- Line: 705

### rspi_data_in
- Return type: static int
- Signature: rspi_data_in(struct rspi_data * rspi)
- Line: 496

### rspi_data_out
- Return type: static int
- Signature: rspi_data_out(struct rspi_data * rspi,u8 data)
- Line: 485

### rspi_disable_irq
- Return type: static void
- Signature: rspi_disable_irq(const struct rspi_data * rspi,u8 disable)
- Line: 453

### rspi_dma_check_then_transfer
- Return type: static int
- Signature: rspi_dma_check_then_transfer(struct rspi_data * rspi,struct spi_transfer * xfer)
- Line: 694

### rspi_dma_complete
- Return type: static void
- Signature: rspi_dma_complete(void * arg)
- Line: 530

### rspi_dma_transfer
- Return type: static int
- Signature: rspi_dma_transfer(struct rspi_data * rspi,struct sg_table * tx,struct sg_table * rx)
- Line: 538

### rspi_enable_irq
- Return type: static void
- Signature: rspi_enable_irq(const struct rspi_data * rspi,u8 enable)
- Line: 448

### rspi_irq_mux
- Return type: static irqreturn_t
- Signature: rspi_irq_mux(int irq,void * _sr)
- Line: 1040

### rspi_irq_rx
- Return type: static irqreturn_t
- Signature: rspi_irq_rx(int irq,void * _sr)
- Line: 1062

### rspi_irq_tx
- Return type: static irqreturn_t
- Signature: rspi_irq_tx(int irq,void * _sr)
- Line: 1077

### rspi_parse_dt
- Return type: static int
- Signature: rspi_parse_dt(struct device * dev,struct spi_controller * ctlr)
- Line: 1270

### rspi_parse_dt
- Return type: static int
- Signature: rspi_parse_dt(struct device * dev,struct spi_controller * ctlr)
- Line: 1234

### rspi_pio_transfer
- Return type: static int
- Signature: rspi_pio_transfer(struct rspi_data * rspi,const u8 * tx,u8 * rx,unsigned int n)
- Line: 510

### rspi_prepare_message
- Return type: static int
- Signature: rspi_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 970

### rspi_probe
- Return type: static int
- Signature: rspi_probe(struct platform_device * pdev)
- Line: 1288

### rspi_read16
- Return type: static u16
- Signature: rspi_read16(const struct rspi_data * rspi,u16 offset)
- Line: 219

### rspi_read8
- Return type: static u8
- Signature: rspi_read8(const struct rspi_data * rspi,u16 offset)
- Line: 214

### rspi_read_data
- Return type: static u16
- Signature: rspi_read_data(const struct rspi_data * rspi)
- Line: 232

### rspi_receive_init
- Return type: static void
- Signature: rspi_receive_init(const struct rspi_data * rspi)
- Line: 650

### rspi_release_dma
- Return type: static void
- Signature: rspi_release_dma(struct spi_controller * ctlr)
- Line: 1162

### rspi_remove
- Return type: static void
- Signature: rspi_remove(struct platform_device * pdev)
- Line: 1170

### rspi_request_dma
- Return type: static int
- Signature: rspi_request_dma(struct device * dev,struct spi_controller * ctlr,const struct resource * res)
- Line: 1130

### rspi_request_dma_chan
- Return type: static dma_chan *
- Signature: rspi_request_dma_chan(struct device * dev,enum dma_transfer_direction dir,unsigned int id,dma_addr_t port_addr)
- Line: 1092

### rspi_request_irq
- Return type: static int
- Signature: rspi_request_irq(struct device * dev,unsigned int irq,irq_handler_t handler,const char * suffix,void * dev_id)
- Line: 1276

### rspi_reset_control_assert
- Return type: static void
- Signature: rspi_reset_control_assert(void * data)
- Line: 1229

### rspi_resume
- Return type: static int
- Signature: rspi_resume(struct device * dev)
- Line: 1419

### rspi_rz_receive_init
- Return type: static void
- Signature: rspi_rz_receive_init(const struct rspi_data * rspi)
- Line: 662

### rspi_rz_set_config_register
- Return type: static int
- Signature: rspi_rz_set_config_register(struct rspi_data * rspi,int access_size)
- Line: 307

### rspi_rz_transfer_one
- Return type: static int
- Signature: rspi_rz_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 744

### rspi_set_config_register
- Return type: static int
- Signature: rspi_set_config_register(struct rspi_data * rspi,int access_size)
- Line: 273

### rspi_set_rate
- Return type: static void
- Signature: rspi_set_rate(struct rspi_data * rspi)
- Line: 253

### rspi_setup
- Return type: static int
- Signature: rspi_setup(struct spi_device * spi)
- Line: 947

### rspi_suspend
- Return type: static int
- Signature: rspi_suspend(struct device * dev)
- Line: 1412

### rspi_transfer_one
- Return type: static int
- Signature: rspi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 726

### rspi_unprepare_message
- Return type: static int
- Signature: rspi_unprepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1026

### rspi_wait_for_interrupt
- Return type: static int
- Signature: rspi_wait_for_interrupt(struct rspi_data * rspi,u8 wait_mask,u8 enable_bit)
- Line: 458

### rspi_wait_for_rx_full
- Return type: static int
- Signature: rspi_wait_for_rx_full(struct rspi_data * rspi)
- Line: 480

### rspi_wait_for_tx_empty
- Return type: static int
- Signature: rspi_wait_for_tx_empty(struct rspi_data * rspi)
- Line: 475

### rspi_write16
- Return type: static void
- Signature: rspi_write16(const struct rspi_data * rspi,u16 data,u16 offset)
- Line: 204

### rspi_write32
- Return type: static void
- Signature: rspi_write32(const struct rspi_data * rspi,u32 data,u16 offset)
- Line: 209

### rspi_write8
- Return type: static void
- Signature: rspi_write8(const struct rspi_data * rspi,u8 data,u16 offset)
- Line: 199

### rspi_write_data
- Return type: static void
- Signature: rspi_write_data(const struct rspi_data * rspi,u16 data)
- Line: 224

## Structs (2)

### rspi_data
- Line: 181
- Members:
  - addr: void __iomem *
  - speed_hz: u32
  - ctlr: spi_controller *
  - pdev: platform_device *
  - wait: wait_queue_head_t
  - lock: spinlock_t
  - clk: clk *
  - spcmd: u16
  - spsr: u8
  - sppcr: u8
  - rx_irq: int
  - tx_irq: int
  - ops: const struct spi_ops *
  - dma_callbacked: unsigned:1
  - byte_access: unsigned:1
  - set_config_register: int (*)(struct rspi_data * rspi,int access_size)
  - transfer_one: int (*)(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
  - extra_mode_bits: u16
  - min_div: u16
  - max_div: u16
  - flags: u16
  - fifo_size: u16
  - num_hw_ss: u8

### spi_ops
- Line: 241
- Members:
  - addr: void __iomem *
  - speed_hz: u32
  - ctlr: spi_controller *
  - pdev: platform_device *
  - wait: wait_queue_head_t
  - lock: spinlock_t
  - clk: clk *
  - spcmd: u16
  - spsr: u8
  - sppcr: u8
  - rx_irq: int
  - tx_irq: int
  - ops: const struct spi_ops *
  - dma_callbacked: unsigned:1
  - byte_access: unsigned:1
  - set_config_register: int (*)(struct rspi_data * rspi,int access_size)
  - transfer_one: int (*)(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
  - extra_mode_bits: u16
  - min_div: u16
  - max_div: u16
  - flags: u16
  - fifo_size: u16
  - num_hw_ss: u8

## Variables (6)

- static **__maybe_unused** : const struct spi_ops qspi_ops (line 1204)
- static **__maybe_unused** : const struct spi_ops rspi_rz_ops (line 1194)
- static **rspi_driver** : platform_driver (line 1428)
- static **rspi_of_match** : const struct of_device_id[]__maybe_unused (line 1216)
- static **rspi_ops** : const struct spi_ops (line 1184)
- static **spi_driver_ids** : const struct platform_device_id[] (line 1405)

## Macros (117)

- **QSPI_BUFFER_SIZE** (line 179)
- **QSPI_NUM_SPCMD** (line 53)
- **QSPI_SPBDCR** (line 61)
- **QSPI_SPBFCR** (line 60)
- **QSPI_SPBMUL**(i) (line 66)
- **QSPI_SPBMUL0** (line 62)
- **QSPI_SPBMUL1** (line 63)
- **QSPI_SPBMUL2** (line 64)
- **QSPI_SPBMUL3** (line 65)
- **RSPI_NUM_SPCMD** (line 51)
- **RSPI_RZ_NUM_SPCMD** (line 52)
- **RSPI_SPBFCR** (line 56)
- **RSPI_SPBFDR** (line 57)
- **RSPI_SPBR** (line 36)
- **RSPI_SPCKD** (line 38)
- **RSPI_SPCMD**(i) (line 50)
- **RSPI_SPCMD0** (line 42)
- **RSPI_SPCMD1** (line 43)
- **RSPI_SPCMD2** (line 44)
- **RSPI_SPCMD3** (line 45)
- **RSPI_SPCMD4** (line 46)
- **RSPI_SPCMD5** (line 47)
- **RSPI_SPCMD6** (line 48)
- **RSPI_SPCMD7** (line 49)
- **RSPI_SPCR** (line 29)
- **RSPI_SPCR2** (line 41)
- **RSPI_SPDCR** (line 37)
- **RSPI_SPDR** (line 33)
- **RSPI_SPND** (line 40)
- **RSPI_SPPCR** (line 31)
- **RSPI_SPSCR** (line 34)
- **RSPI_SPSR** (line 32)
- **RSPI_SPSSR** (line 35)
- **RSPI_SSLND** (line 39)
- **RSPI_SSLP** (line 30)
- **SPBFCR_RXRST** (line 170)
- **SPBFCR_RXTRG_1B** (line 176)
- **SPBFCR_RXTRG_32B** (line 177)
- **SPBFCR_RXTRG_MASK** (line 172)
- **SPBFCR_TXRST** (line 169)
- **SPBFCR_TXTRG_1B** (line 174)
- **SPBFCR_TXTRG_32B** (line 175)
- **SPBFCR_TXTRG_MASK** (line 171)
- **SPCKD_SCKDL_MASK** (line 128)
- **SPCMD_BRDV**(brdv) (line 164)
- **SPCMD_BRDV_MASK** (line 163)
- **SPCMD_CPHA** (line 166)
- **SPCMD_CPOL** (line 165)
- **SPCMD_LSBF** (line 146)
- **SPCMD_SCKDEN** (line 143)
- **SPCMD_SLNDEN** (line 144)
- **SPCMD_SPB_16BIT** (line 150)
- **SPCMD_SPB_20BIT** (line 151)
- **SPCMD_SPB_24BIT** (line 152)
- **SPCMD_SPB_32BIT** (line 153)
- **SPCMD_SPB_8BIT** (line 149)
- **SPCMD_SPB_8_TO_16**(bit) (line 148)
- **SPCMD_SPB_MASK** (line 147)
- **SPCMD_SPIMOD0** (line 157)
- **SPCMD_SPIMOD1** (line 156)
- **SPCMD_SPIMOD_DUAL** (line 159)
- **SPCMD_SPIMOD_MASK** (line 155)
- **SPCMD_SPIMOD_QUAD** (line 160)
- **SPCMD_SPIMOD_SINGLE** (line 158)
- **SPCMD_SPNDEN** (line 145)
- **SPCMD_SPRW** (line 161)
- **SPCMD_SSLA**(i) (line 162)
- **SPCMD_SSLKP** (line 154)
- **SPCR2_PTE** (line 137)
- **SPCR2_SPIE** (line 138)
- **SPCR2_SPOE** (line 139)
- **SPCR2_SPPE** (line 140)
- **SPCR_BSWAP** (line 80)
- **SPCR_MODFEN** (line 74)
- **SPCR_MSTR** (line 73)
- **SPCR_SPE** (line 70)
- **SPCR_SPEIE** (line 72)
- **SPCR_SPMS** (line 77)
- **SPCR_SPRIE** (line 69)
- **SPCR_SPTIE** (line 71)
- **SPCR_TXMD** (line 76)
- **SPCR_WSWAP** (line 79)
- **SPDCR_SLSEL0** (line 121)
- **SPDCR_SLSEL1** (line 120)
- **SPDCR_SLSEL_MASK** (line 122)
- **SPDCR_SPFC0** (line 124)
- **SPDCR_SPFC1** (line 123)
- **SPDCR_SPFC_MASK** (line 125)
- **SPDCR_SPLBYTE** (line 117)
- **SPDCR_SPLLWORD** (line 115)
- **SPDCR_SPLW** (line 118)
- **SPDCR_SPLW0** (line 114)
- **SPDCR_SPLW1** (line 113)
- **SPDCR_SPLWORD** (line 116)
- **SPDCR_SPRDTD** (line 119)
- **SPDCR_TXDMY** (line 112)
- **SPND_SPNDL_MASK** (line 134)
- **SPPCR_IO2FV** (line 93)
- **SPPCR_IO3FV** (line 92)
- **SPPCR_MOIFE** (line 86)
- **SPPCR_MOIFV** (line 87)
- **SPPCR_SPLP** (line 90)
- **SPPCR_SPLP2** (line 89)
- **SPPCR_SPOM** (line 88)
- **SPSCR_SPSLN_MASK** (line 105)
- **SPSR_IDLNF** (line 101)
- **SPSR_MODF** (line 100)
- **SPSR_OVRF** (line 102)
- **SPSR_PERF** (line 99)
- **SPSR_SPRF** (line 96)
- **SPSR_SPTEF** (line 98)
- **SPSR_TEND** (line 97)
- **SPSSR_SPCP_MASK** (line 109)
- **SPSSR_SPECM_MASK** (line 108)
- **SSLND_SLNDL_MASK** (line 131)
- **SSLP_SSLP**(i) (line 83)
- **rspi_of_match** (line 1269)
