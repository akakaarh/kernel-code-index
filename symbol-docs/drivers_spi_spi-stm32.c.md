# drivers/spi/spi-stm32.c

Subsystem: drivers/spi

## Functions (57)

### stm32_spi_can_dma
- Return type: static bool
- Signature: stm32_spi_can_dma(struct spi_controller * ctrl,struct spi_device * spi_dev,struct spi_transfer * transfer)
- Line: 934

### stm32_spi_can_poll
- Return type: static bool
- Signature: stm32_spi_can_poll(struct stm32_spi * spi)
- Line: 2093

### stm32_spi_clr_bits
- Return type: static void
- Signature: stm32_spi_clr_bits(struct stm32_spi * spi,u32 offset,u32 bits)
- Line: 453

### stm32_spi_communication_type
- Return type: static unsigned int
- Signature: stm32_spi_communication_type(struct spi_device * spi_dev,struct spi_transfer * transfer)
- Line: 1850

### stm32_spi_dma_config
- Return type: static void
- Signature: stm32_spi_dma_config(struct stm32_spi * spi,struct dma_chan * dma_chan,struct dma_slave_config * dma_conf,enum dma_transfer_direction dir)
- Line: 1276

### stm32_spi_dma_rx_cb
- Return type: static void
- Signature: stm32_spi_dma_rx_cb(void * data)
- Line: 1260

### stm32_spi_enable
- Return type: static void
- Signature: stm32_spi_enable(struct stm32_spi * spi)
- Line: 823

### stm32_spi_optimize_message
- Return type: static int
- Signature: stm32_spi_optimize_message(struct spi_message * msg)
- Line: 1158

### stm32_spi_prepare_mbr
- Return type: static int
- Signature: stm32_spi_prepare_mbr(struct stm32_spi * spi,u32 speed_hz,u32 min_div,u32 max_div)
- Line: 563

### stm32_spi_prepare_msg
- Return type: static int
- Signature: stm32_spi_prepare_msg(struct spi_controller * ctrl,struct spi_message * msg)
- Line: 1178

### stm32_spi_prepare_rx_dma_mdma_chaining
- Return type: static int
- Signature: stm32_spi_prepare_rx_dma_mdma_chaining(struct stm32_spi * spi,struct spi_transfer * xfer,struct dma_slave_config * rx_dma_conf,struct dma_async_tx_descriptor ** rx_dma_desc,struct dma_async_tx_descriptor ** rx_mdma_desc)
- Line: 1526

### stm32_spi_probe
- Return type: static int
- Signature: stm32_spi_probe(struct platform_device * pdev)
- Line: 2351

### stm32_spi_remove
- Return type: static void
- Signature: stm32_spi_remove(struct platform_device * pdev)
- Line: 2563

### stm32_spi_resume
- Return type: static int
- Signature: stm32_spi_resume(struct device * dev)
- Line: 2626

### stm32_spi_runtime_resume
- Return type: static int
- Signature: stm32_spi_runtime_resume(struct device * dev)
- Line: 2601

### stm32_spi_runtime_suspend
- Return type: static int
- Signature: stm32_spi_runtime_suspend(struct device * dev)
- Line: 2591

### stm32_spi_set_bits
- Return type: static void
- Signature: stm32_spi_set_bits(struct stm32_spi * spi,u32 offset,u32 bits)
- Line: 446

### stm32_spi_set_mbr
- Return type: static void
- Signature: stm32_spi_set_mbr(struct stm32_spi * spi,u32 mbrdiv)
- Line: 1833

### stm32_spi_suspend
- Return type: static int
- Signature: stm32_spi_suspend(struct device * dev)
- Line: 2614

### stm32_spi_transfer_one
- Return type: static int
- Signature: stm32_spi_transfer_one(struct spi_controller * ctrl,struct spi_device * spi_dev,struct spi_transfer * transfer)
- Line: 2114

### stm32_spi_transfer_one_dma
- Return type: static int
- Signature: stm32_spi_transfer_one_dma(struct stm32_spi * spi,struct spi_transfer * xfer)
- Line: 1642

### stm32_spi_transfer_one_setup
- Return type: static int
- Signature: stm32_spi_transfer_one_setup(struct stm32_spi * spi,struct spi_device * spi_dev,struct spi_transfer * transfer)
- Line: 2009

### stm32_spi_unprepare_msg
- Return type: static int
- Signature: stm32_spi_unprepare_msg(struct spi_controller * ctrl,struct spi_message * msg)
- Line: 2148

### stm32f4_spi_get_bpw_mask
- Return type: static int
- Signature: stm32f4_spi_get_bpw_mask(struct stm32_spi * spi)
- Line: 489

### stm32f4_spi_read_rx
- Return type: static void
- Signature: stm32f4_spi_read_rx(struct stm32_spi * spi)
- Line: 711

### stm32f4_spi_set_bpw
- Return type: static void
- Signature: stm32f4_spi_set_bpw(struct stm32_spi * spi)
- Line: 1769

### stm32f4_spi_write_tx
- Return type: static void
- Signature: stm32f4_spi_write_tx(struct stm32_spi * spi)
- Line: 618

### stm32f7_spi_get_bpw_mask
- Return type: static int
- Signature: stm32f7_spi_get_bpw_mask(struct stm32_spi * spi)
- Line: 499

### stm32f7_spi_read_rx
- Return type: static void
- Signature: stm32f7_spi_read_rx(struct stm32_spi * spi)
- Line: 740

### stm32f7_spi_set_bpw
- Return type: static void
- Signature: stm32f7_spi_set_bpw(struct stm32_spi * spi)
- Line: 1781

### stm32f7_spi_transfer_one_dma_start
- Return type: static void
- Signature: stm32f7_spi_transfer_one_dma_start(struct stm32_spi * spi)
- Line: 1482

### stm32f7_spi_write_tx
- Return type: static void
- Signature: stm32f7_spi_write_tx(struct stm32_spi * spi)
- Line: 647

### stm32fx_spi_config
- Return type: static int
- Signature: stm32fx_spi_config(struct stm32_spi * spi)
- Line: 2165

### stm32fx_spi_disable
- Return type: static void
- Signature: stm32fx_spi_disable(struct stm32_spi * spi)
- Line: 835

### stm32fx_spi_dma_tx_cb
- Return type: static void
- Signature: stm32fx_spi_dma_tx_cb(void * data)
- Line: 1244

### stm32fx_spi_irq_event
- Return type: static irqreturn_t
- Signature: stm32fx_spi_irq_event(int irq,void * dev_id)
- Line: 957

### stm32fx_spi_irq_thread
- Return type: static irqreturn_t
- Signature: stm32fx_spi_irq_thread(int irq,void * dev_id)
- Line: 1045

### stm32fx_spi_set_mode
- Return type: static int
- Signature: stm32fx_spi_set_mode(struct stm32_spi * spi,unsigned int comm_type)
- Line: 1881

### stm32fx_spi_transfer_one_dma_start
- Return type: static void
- Signature: stm32fx_spi_transfer_one_dma_start(struct stm32_spi * spi)
- Line: 1461

### stm32fx_spi_transfer_one_irq
- Return type: static int
- Signature: stm32fx_spi_transfer_one_irq(struct stm32_spi * spi)
- Line: 1329

### stm32h7_spi_config
- Return type: static int
- Signature: stm32h7_spi_config(struct stm32_spi * spi)
- Line: 2196

### stm32h7_spi_data_idleness
- Return type: static void
- Signature: stm32h7_spi_data_idleness(struct stm32_spi * spi,struct spi_transfer * xfer)
- Line: 1945

### stm32h7_spi_device_abort
- Return type: static int
- Signature: stm32h7_spi_device_abort(struct spi_controller * ctrl)
- Line: 2345

### stm32h7_spi_disable
- Return type: static void
- Signature: stm32h7_spi_disable(struct stm32_spi * spi)
- Line: 885

### stm32h7_spi_get_bpw_mask
- Return type: static int
- Signature: stm32h7_spi_get_bpw_mask(struct stm32_spi * spi)
- Line: 509

### stm32h7_spi_get_fifo_size
- Return type: static int
- Signature: stm32h7_spi_get_fifo_size(struct stm32_spi * spi)
- Line: 464

### stm32h7_spi_irq_thread
- Return type: static irqreturn_t
- Signature: stm32h7_spi_irq_thread(int irq,void * dev_id)
- Line: 1061

### stm32h7_spi_number_of_data
- Return type: static int
- Signature: stm32h7_spi_number_of_data(struct stm32_spi * spi,u32 nb_words)
- Line: 1989

### stm32h7_spi_prepare_fthlv
- Return type: static u32
- Signature: stm32h7_spi_prepare_fthlv(struct stm32_spi * spi,u32 xfer_len)
- Line: 599

### stm32h7_spi_read_rxfifo
- Return type: static void
- Signature: stm32h7_spi_read_rxfifo(struct stm32_spi * spi)
- Line: 780

### stm32h7_spi_set_bpw
- Return type: static void
- Signature: stm32h7_spi_set_bpw(struct stm32_spi * spi)
- Line: 1806

### stm32h7_spi_set_mode
- Return type: static int
- Signature: stm32h7_spi_set_mode(struct stm32_spi * spi,unsigned int comm_type)
- Line: 1909

### stm32h7_spi_transfer_one_dma_start
- Return type: static void
- Signature: stm32h7_spi_transfer_one_dma_start(struct stm32_spi * spi)
- Line: 1498

### stm32h7_spi_transfer_one_irq
- Return type: static int
- Signature: stm32h7_spi_transfer_one_irq(struct stm32_spi * spi)
- Line: 1421

### stm32h7_spi_transfer_one_poll
- Return type: static int
- Signature: stm32h7_spi_transfer_one_poll(struct stm32_spi * spi)
- Line: 1372

### stm32h7_spi_write_txfifo
- Return type: static void
- Signature: stm32h7_spi_write_txfifo(struct stm32_spi * spi)
- Line: 676

### stm32mp25_spi_get_bpw_mask
- Return type: static int
- Signature: stm32mp25_spi_get_bpw_mask(struct stm32_spi * spi)
- Line: 536

## Structs (4)

### stm32_spi
- Line: 345
- Members:
  - reg: int
  - mask: int
  - shift: int
  - en: const struct stm32_spi_reg
  - dma_rx_en: const struct stm32_spi_reg
  - dma_tx_en: const struct stm32_spi_reg
  - cpol: const struct stm32_spi_reg
  - cpha: const struct stm32_spi_reg
  - lsb_first: const struct stm32_spi_reg
  - cs_high: const struct stm32_spi_reg
  - br: const struct stm32_spi_reg
  - rx: const struct stm32_spi_reg
  - tx: const struct stm32_spi_reg
  - fullcfg: const struct stm32_spi_reg
  - rdy_en: const struct stm32_spi_reg
  - regs: const struct stm32_spi_regspec *
  - get_fifo_size: int (*)(struct stm32_spi * spi)
  - get_bpw_mask: int (*)(struct stm32_spi * spi)
  - disable: void (*)(struct stm32_spi * spi)
  - config: int (*)(struct stm32_spi * spi)
  - set_bpw: void (*)(struct stm32_spi * spi)
  - set_mode: int (*)(struct stm32_spi * spi,unsigned int comm_type)
  - set_data_idleness: void (*)(struct stm32_spi * spi,struct spi_transfer * xfer)
  - set_number_of_data: int (*)(struct stm32_spi * spi,u32 length)
  - write_tx: void (*)(struct stm32_spi * spi)
  - read_rx: void (*)(struct stm32_spi * spi)
  - transfer_one_dma_start: void (*)(struct stm32_spi * spi)
  - dma_rx_cb: void (*)(void * data)
  - dma_tx_cb: void (*)(void * data)
  - transfer_one_irq: int (*)(struct stm32_spi * spi)
  - transfer_one_poll: int (*)(struct stm32_spi * spi)
  - irq_handler_event: irqreturn_t (*)(int irq,void * dev_id)
  - irq_handler_thread: irqreturn_t (*)(int irq,void * dev_id)
  - baud_rate_div_min: unsigned int
  - baud_rate_div_max: unsigned int
  - has_fifo: bool
  - has_device_mode: bool
  - flags: u16
  - prevent_dma_burst: bool
  - dev: device *
  - ctrl: spi_controller *
  - cfg: const struct stm32_spi_cfg *
  - base: void __iomem *
  - clk: clk *
  - clk_rate: u32
  - lock: spinlock_t
  - irq: int
  - fifo_size: unsigned int
  - t_size_max: unsigned int
  - feature_set: unsigned int
  - cur_midi: unsigned int
  - cur_speed: unsigned int
  - cur_half_period: unsigned int
  - cur_bpw: unsigned int
  - cur_fthlv: unsigned int
  - cur_comm: unsigned int
  - cur_xferlen: unsigned int
  - cur_usedma: bool
  - tx_buf: const void *
  - rx_buf: void *
  - tx_len: int
  - rx_len: int
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - phys_addr: dma_addr_t
  - device_mode: bool
  - sram_pool: gen_pool *
  - sram_rx_buf_size: size_t
  - sram_rx_buf: void *
  - sram_dma_rx_buf: dma_addr_t
  - mdma_rx: dma_chan *

### stm32_spi_cfg
- Line: 283
- Members:
  - reg: int
  - mask: int
  - shift: int
  - en: const struct stm32_spi_reg
  - dma_rx_en: const struct stm32_spi_reg
  - dma_tx_en: const struct stm32_spi_reg
  - cpol: const struct stm32_spi_reg
  - cpha: const struct stm32_spi_reg
  - lsb_first: const struct stm32_spi_reg
  - cs_high: const struct stm32_spi_reg
  - br: const struct stm32_spi_reg
  - rx: const struct stm32_spi_reg
  - tx: const struct stm32_spi_reg
  - fullcfg: const struct stm32_spi_reg
  - rdy_en: const struct stm32_spi_reg
  - regs: const struct stm32_spi_regspec *
  - get_fifo_size: int (*)(struct stm32_spi * spi)
  - get_bpw_mask: int (*)(struct stm32_spi * spi)
  - disable: void (*)(struct stm32_spi * spi)
  - config: int (*)(struct stm32_spi * spi)
  - set_bpw: void (*)(struct stm32_spi * spi)
  - set_mode: int (*)(struct stm32_spi * spi,unsigned int comm_type)
  - set_data_idleness: void (*)(struct stm32_spi * spi,struct spi_transfer * xfer)
  - set_number_of_data: int (*)(struct stm32_spi * spi,u32 length)
  - write_tx: void (*)(struct stm32_spi * spi)
  - read_rx: void (*)(struct stm32_spi * spi)
  - transfer_one_dma_start: void (*)(struct stm32_spi * spi)
  - dma_rx_cb: void (*)(void * data)
  - dma_tx_cb: void (*)(void * data)
  - transfer_one_irq: int (*)(struct stm32_spi * spi)
  - transfer_one_poll: int (*)(struct stm32_spi * spi)
  - irq_handler_event: irqreturn_t (*)(int irq,void * dev_id)
  - irq_handler_thread: irqreturn_t (*)(int irq,void * dev_id)
  - baud_rate_div_min: unsigned int
  - baud_rate_div_max: unsigned int
  - has_fifo: bool
  - has_device_mode: bool
  - flags: u16
  - prevent_dma_burst: bool
  - dev: device *
  - ctrl: spi_controller *
  - cfg: const struct stm32_spi_cfg *
  - base: void __iomem *
  - clk: clk *
  - clk_rate: u32
  - lock: spinlock_t
  - irq: int
  - fifo_size: unsigned int
  - t_size_max: unsigned int
  - feature_set: unsigned int
  - cur_midi: unsigned int
  - cur_speed: unsigned int
  - cur_half_period: unsigned int
  - cur_bpw: unsigned int
  - cur_fthlv: unsigned int
  - cur_comm: unsigned int
  - cur_xferlen: unsigned int
  - cur_usedma: bool
  - tx_buf: const void *
  - rx_buf: void *
  - tx_len: int
  - rx_len: int
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - phys_addr: dma_addr_t
  - device_mode: bool
  - sram_pool: gen_pool *
  - sram_rx_buf_size: size_t
  - sram_rx_buf: void *
  - sram_dma_rx_buf: dma_addr_t
  - mdma_rx: dma_chan *

### stm32_spi_reg
- Line: 215
- Members:
  - reg: int
  - mask: int
  - shift: int
  - en: const struct stm32_spi_reg
  - dma_rx_en: const struct stm32_spi_reg
  - dma_tx_en: const struct stm32_spi_reg
  - cpol: const struct stm32_spi_reg
  - cpha: const struct stm32_spi_reg
  - lsb_first: const struct stm32_spi_reg
  - cs_high: const struct stm32_spi_reg
  - br: const struct stm32_spi_reg
  - rx: const struct stm32_spi_reg
  - tx: const struct stm32_spi_reg
  - fullcfg: const struct stm32_spi_reg
  - rdy_en: const struct stm32_spi_reg
  - regs: const struct stm32_spi_regspec *
  - get_fifo_size: int (*)(struct stm32_spi * spi)
  - get_bpw_mask: int (*)(struct stm32_spi * spi)
  - disable: void (*)(struct stm32_spi * spi)
  - config: int (*)(struct stm32_spi * spi)
  - set_bpw: void (*)(struct stm32_spi * spi)
  - set_mode: int (*)(struct stm32_spi * spi,unsigned int comm_type)
  - set_data_idleness: void (*)(struct stm32_spi * spi,struct spi_transfer * xfer)
  - set_number_of_data: int (*)(struct stm32_spi * spi,u32 length)
  - write_tx: void (*)(struct stm32_spi * spi)
  - read_rx: void (*)(struct stm32_spi * spi)
  - transfer_one_dma_start: void (*)(struct stm32_spi * spi)
  - dma_rx_cb: void (*)(void * data)
  - dma_tx_cb: void (*)(void * data)
  - transfer_one_irq: int (*)(struct stm32_spi * spi)
  - transfer_one_poll: int (*)(struct stm32_spi * spi)
  - irq_handler_event: irqreturn_t (*)(int irq,void * dev_id)
  - irq_handler_thread: irqreturn_t (*)(int irq,void * dev_id)
  - baud_rate_div_min: unsigned int
  - baud_rate_div_max: unsigned int
  - has_fifo: bool
  - has_device_mode: bool
  - flags: u16
  - prevent_dma_burst: bool
  - dev: device *
  - ctrl: spi_controller *
  - cfg: const struct stm32_spi_cfg *
  - base: void __iomem *
  - clk: clk *
  - clk_rate: u32
  - lock: spinlock_t
  - irq: int
  - fifo_size: unsigned int
  - t_size_max: unsigned int
  - feature_set: unsigned int
  - cur_midi: unsigned int
  - cur_speed: unsigned int
  - cur_half_period: unsigned int
  - cur_bpw: unsigned int
  - cur_fthlv: unsigned int
  - cur_comm: unsigned int
  - cur_xferlen: unsigned int
  - cur_usedma: bool
  - tx_buf: const void *
  - rx_buf: void *
  - tx_len: int
  - rx_len: int
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - phys_addr: dma_addr_t
  - device_mode: bool
  - sram_pool: gen_pool *
  - sram_rx_buf_size: size_t
  - sram_rx_buf: void *
  - sram_dma_rx_buf: dma_addr_t
  - mdma_rx: dma_chan *

### stm32_spi_regspec
- Line: 236
- Members:
  - reg: int
  - mask: int
  - shift: int
  - en: const struct stm32_spi_reg
  - dma_rx_en: const struct stm32_spi_reg
  - dma_tx_en: const struct stm32_spi_reg
  - cpol: const struct stm32_spi_reg
  - cpha: const struct stm32_spi_reg
  - lsb_first: const struct stm32_spi_reg
  - cs_high: const struct stm32_spi_reg
  - br: const struct stm32_spi_reg
  - rx: const struct stm32_spi_reg
  - tx: const struct stm32_spi_reg
  - fullcfg: const struct stm32_spi_reg
  - rdy_en: const struct stm32_spi_reg
  - regs: const struct stm32_spi_regspec *
  - get_fifo_size: int (*)(struct stm32_spi * spi)
  - get_bpw_mask: int (*)(struct stm32_spi * spi)
  - disable: void (*)(struct stm32_spi * spi)
  - config: int (*)(struct stm32_spi * spi)
  - set_bpw: void (*)(struct stm32_spi * spi)
  - set_mode: int (*)(struct stm32_spi * spi,unsigned int comm_type)
  - set_data_idleness: void (*)(struct stm32_spi * spi,struct spi_transfer * xfer)
  - set_number_of_data: int (*)(struct stm32_spi * spi,u32 length)
  - write_tx: void (*)(struct stm32_spi * spi)
  - read_rx: void (*)(struct stm32_spi * spi)
  - transfer_one_dma_start: void (*)(struct stm32_spi * spi)
  - dma_rx_cb: void (*)(void * data)
  - dma_tx_cb: void (*)(void * data)
  - transfer_one_irq: int (*)(struct stm32_spi * spi)
  - transfer_one_poll: int (*)(struct stm32_spi * spi)
  - irq_handler_event: irqreturn_t (*)(int irq,void * dev_id)
  - irq_handler_thread: irqreturn_t (*)(int irq,void * dev_id)
  - baud_rate_div_min: unsigned int
  - baud_rate_div_max: unsigned int
  - has_fifo: bool
  - has_device_mode: bool
  - flags: u16
  - prevent_dma_burst: bool
  - dev: device *
  - ctrl: spi_controller *
  - cfg: const struct stm32_spi_cfg *
  - base: void __iomem *
  - clk: clk *
  - clk_rate: u32
  - lock: spinlock_t
  - irq: int
  - fifo_size: unsigned int
  - t_size_max: unsigned int
  - feature_set: unsigned int
  - cur_midi: unsigned int
  - cur_speed: unsigned int
  - cur_half_period: unsigned int
  - cur_bpw: unsigned int
  - cur_fthlv: unsigned int
  - cur_comm: unsigned int
  - cur_xferlen: unsigned int
  - cur_usedma: bool
  - tx_buf: const void *
  - rx_buf: void *
  - tx_len: int
  - rx_len: int
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - phys_addr: dma_addr_t
  - device_mode: bool
  - sram_pool: gen_pool *
  - sram_rx_buf_size: size_t
  - sram_rx_buf: void *
  - sram_dma_rx_buf: dma_addr_t
  - mdma_rx: dma_chan *

## Variables (11)

- static **polling_limit_us** : unsigned int (line 205)
- static **stm32_spi_driver** : platform_driver (line 2660)
- static **stm32_spi_of_match** : const struct of_device_id[] (line 2336)
- static **stm32_spi_pm_ops** : const struct dev_pm_ops (line 2655)
- static **stm32f4_spi_cfg** : const struct stm32_spi_cfg (line 2235)
- static **stm32f7_spi_cfg** : const struct stm32_spi_cfg (line 2257)
- static **stm32fx_spi_regspec** : const struct stm32_spi_regspec (line 386)
- static **stm32h7_spi_cfg** : const struct stm32_spi_cfg (line 2278)
- static **stm32h7_spi_regspec** : const struct stm32_spi_regspec (line 402)
- static **stm32mp25_spi_cfg** : const struct stm32_spi_cfg (line 2310)
- static **stm32mp25_spi_regspec** : const struct stm32_spi_regspec (line 422)

## Macros (129)

- **DRIVER_NAME** (line 25)
- **SPI_3WIRE_RX** (line 191)
- **SPI_3WIRE_TX** (line 190)
- **SPI_DMA_MIN_BYTES** (line 199)
- **SPI_FULL_DUPLEX** (line 187)
- **SPI_SIMPLEX_RX** (line 189)
- **SPI_SIMPLEX_TX** (line 188)
- **STM32F4_SPI_CR1_DFF** (line 45)
- **STM32F7_SPI_CR1_CRCL** (line 46)
- **STM32F7_SPI_CR2_DS** (line 62)
- **STM32F7_SPI_CR2_FRXTH** (line 63)
- **STM32F7_SPI_CR2_LDMA_RX** (line 64)
- **STM32F7_SPI_CR2_LDMA_TX** (line 65)
- **STM32F7_SPI_SR_FRLVL** (line 77)
- **STM32F7_SPI_SR_FTLVL** (line 78)
- **STM32FX_SPI_BR_DIV_MAX** (line 85)
- **STM32FX_SPI_BR_DIV_MIN** (line 84)
- **STM32FX_SPI_CR1** (line 28)
- **STM32FX_SPI_CR1_BIDIMODE** (line 50)
- **STM32FX_SPI_CR1_BIDIOE** (line 49)
- **STM32FX_SPI_CR1_BR** (line 39)
- **STM32FX_SPI_CR1_BR_MAX** (line 52)
- **STM32FX_SPI_CR1_BR_MIN** (line 51)
- **STM32FX_SPI_CR1_BR_SHIFT** (line 38)
- **STM32FX_SPI_CR1_CPHA** (line 35)
- **STM32FX_SPI_CR1_CPOL** (line 36)
- **STM32FX_SPI_CR1_CRCEN** (line 48)
- **STM32FX_SPI_CR1_CRCNEXT** (line 47)
- **STM32FX_SPI_CR1_LSBFRST** (line 41)
- **STM32FX_SPI_CR1_MSTR** (line 37)
- **STM32FX_SPI_CR1_RXONLY** (line 44)
- **STM32FX_SPI_CR1_SPE** (line 40)
- **STM32FX_SPI_CR1_SSI** (line 42)
- **STM32FX_SPI_CR1_SSM** (line 43)
- **STM32FX_SPI_CR2** (line 29)
- **STM32FX_SPI_CR2_ERRIE** (line 59)
- **STM32FX_SPI_CR2_FRF** (line 58)
- **STM32FX_SPI_CR2_RXDMAEN** (line 55)
- **STM32FX_SPI_CR2_RXNEIE** (line 60)
- **STM32FX_SPI_CR2_SSOE** (line 57)
- **STM32FX_SPI_CR2_TXDMAEN** (line 56)
- **STM32FX_SPI_CR2_TXEIE** (line 61)
- **STM32FX_SPI_DR** (line 31)
- **STM32FX_SPI_I2SCFGR** (line 32)
- **STM32FX_SPI_I2SCFGR_I2SMOD** (line 81)
- **STM32FX_SPI_SR** (line 30)
- **STM32FX_SPI_SR_BSY** (line 75)
- **STM32FX_SPI_SR_CHSIDE** (line 70)
- **STM32FX_SPI_SR_CRCERR** (line 72)
- **STM32FX_SPI_SR_FRE** (line 76)
- **STM32FX_SPI_SR_MODF** (line 73)
- **STM32FX_SPI_SR_OVR** (line 74)
- **STM32FX_SPI_SR_RXNE** (line 68)
- **STM32FX_SPI_SR_TXE** (line 69)
- **STM32FX_SPI_SR_UDR** (line 71)
- **STM32H7_SPI_CFG1** (line 90)
- **STM32H7_SPI_CFG1_DSIZE** (line 112)
- **STM32H7_SPI_CFG1_FTHLV** (line 113)
- **STM32H7_SPI_CFG1_MBR** (line 116)
- **STM32H7_SPI_CFG1_MBR_MAX** (line 119)
- **STM32H7_SPI_CFG1_MBR_MIN** (line 118)
- **STM32H7_SPI_CFG1_MBR_SHIFT** (line 117)
- **STM32H7_SPI_CFG1_RXDMAEN** (line 114)
- **STM32H7_SPI_CFG1_TXDMAEN** (line 115)
- **STM32H7_SPI_CFG2** (line 91)
- **STM32H7_SPI_CFG2_AFCNTR** (line 131)
- **STM32H7_SPI_CFG2_COMM** (line 123)
- **STM32H7_SPI_CFG2_CPHA** (line 127)
- **STM32H7_SPI_CFG2_CPOL** (line 128)
- **STM32H7_SPI_CFG2_LSBFRST** (line 126)
- **STM32H7_SPI_CFG2_MASTER** (line 125)
- **STM32H7_SPI_CFG2_MIDI** (line 122)
- **STM32H7_SPI_CFG2_SP** (line 124)
- **STM32H7_SPI_CFG2_SSIOP** (line 130)
- **STM32H7_SPI_CFG2_SSM** (line 129)
- **STM32H7_SPI_CR1** (line 88)
- **STM32H7_SPI_CR1_CSTART** (line 102)
- **STM32H7_SPI_CR1_CSUSP** (line 103)
- **STM32H7_SPI_CR1_HDDIR** (line 104)
- **STM32H7_SPI_CR1_MASRX** (line 101)
- **STM32H7_SPI_CR1_SPE** (line 100)
- **STM32H7_SPI_CR1_SSI** (line 105)
- **STM32H7_SPI_CR2** (line 89)
- **STM32H7_SPI_CR2_TSIZE** (line 108)
- **STM32H7_SPI_FULL_DUPLEX** (line 181)
- **STM32H7_SPI_HALF_DUPLEX** (line 184)
- **STM32H7_SPI_I2SCFGR** (line 97)
- **STM32H7_SPI_I2SCFGR_I2SMOD** (line 157)
- **STM32H7_SPI_IER** (line 92)
- **STM32H7_SPI_IER_ALL** (line 141)
- **STM32H7_SPI_IER_DXPIE** (line 136)
- **STM32H7_SPI_IER_EOTIE** (line 137)
- **STM32H7_SPI_IER_MODFIE** (line 140)
- **STM32H7_SPI_IER_OVRIE** (line 139)
- **STM32H7_SPI_IER_RXPIE** (line 134)
- **STM32H7_SPI_IER_TXPIE** (line 135)
- **STM32H7_SPI_IER_TXTFIE** (line 138)
- **STM32H7_SPI_IFCR** (line 94)
- **STM32H7_SPI_IFCR_ALL** (line 154)
- **STM32H7_SPI_MBR_DIV_MAX** (line 178)
- **STM32H7_SPI_MBR_DIV_MIN** (line 177)
- **STM32H7_SPI_RXDR** (line 96)
- **STM32H7_SPI_SIMPLEX_RX** (line 183)
- **STM32H7_SPI_SIMPLEX_TX** (line 182)
- **STM32H7_SPI_SR** (line 93)
- **STM32H7_SPI_SR_EOT** (line 146)
- **STM32H7_SPI_SR_MODF** (line 148)
- **STM32H7_SPI_SR_OVR** (line 147)
- **STM32H7_SPI_SR_RXP** (line 144)
- **STM32H7_SPI_SR_RXPLVL** (line 150)
- **STM32H7_SPI_SR_RXWNE** (line 151)
- **STM32H7_SPI_SR_SUSP** (line 149)
- **STM32H7_SPI_SR_TXP** (line 145)
- **STM32H7_SPI_TSIZE_MAX** (line 109)
- **STM32H7_SPI_TXDR** (line 95)
- **STM32MP25_SPI_CFG2_RDIOM** (line 160)
- **STM32MP25_SPI_HWCFGR1** (line 163)
- **STM32MP25_SPI_HWCFGR1_DSCFG** (line 172)
- **STM32MP25_SPI_HWCFGR1_DSCFG_16_B** (line 173)
- **STM32MP25_SPI_HWCFGR1_DSCFG_32_B** (line 174)
- **STM32MP25_SPI_HWCFGR1_FULLCFG** (line 169)
- **STM32MP25_SPI_HWCFGR1_FULLCFG_FULL** (line 171)
- **STM32MP25_SPI_HWCFGR1_FULLCFG_LIMITED** (line 170)
- **STM32MP25_SPI_TSIZE_MAX_LIMITED** (line 166)
- **STM32_SPI_AUTOSUSPEND_DELAY** (line 193)
- **STM32_SPI_DEVICE_MODE**(stm32_spi) (line 203)
- **STM32_SPI_FEATURE_FULL** (line 358)
- **STM32_SPI_FEATURE_LIMITED** (line 357)
- **STM32_SPI_HOST_MODE**(stm32_spi) (line 202)
