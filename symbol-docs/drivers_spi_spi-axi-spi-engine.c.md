# drivers/spi/spi-axi-spi-engine.c

Subsystem: drivers/spi

## Functions (30)

### spi_engine_all_lanes_flags
- Return type: static void
- Signature: spi_engine_all_lanes_flags(struct spi_device * spi,u8 * rx_lane_flags,u8 * tx_lane_flags)
- Line: 189

### spi_engine_compile_message
- Return type: static void
- Signature: spi_engine_compile_message(struct spi_message * msg,bool dry,struct spi_engine_program * p)
- Line: 368

### spi_engine_gen_cs
- Return type: static void
- Signature: spi_engine_gen_cs(struct spi_engine_program * p,bool dry,struct spi_device * spi,bool assert)
- Line: 281

### spi_engine_gen_sleep
- Return type: static void
- Signature: spi_engine_gen_sleep(struct spi_engine_program * p,bool dry,int delay_ns,int inst_ns,u32 sclk_hz)
- Line: 258

### spi_engine_gen_xfer
- Return type: static void
- Signature: spi_engine_gen_xfer(struct spi_engine_program * p,bool dry,struct spi_transfer * xfer,u32 num_lanes)
- Line: 228

### spi_engine_get_config
- Return type: static unsigned int
- Signature: spi_engine_get_config(struct spi_device * spi)
- Line: 210

### spi_engine_get_offload
- Return type: static spi_offload *
- Signature: spi_engine_get_offload(struct spi_device * spi,const struct spi_offload_config * config)
- Line: 857

### spi_engine_irq
- Return type: static irqreturn_t
- Signature: spi_engine_irq(int irq,void * devid)
- Line: 658

### spi_engine_offload_prepare
- Return type: static int
- Signature: spi_engine_offload_prepare(struct spi_message * msg)
- Line: 713

### spi_engine_offload_unprepare
- Return type: static void
- Signature: spi_engine_offload_unprepare(struct spi_offload * offload)
- Line: 791

### spi_engine_optimize_message
- Return type: static int
- Signature: spi_engine_optimize_message(struct spi_message * msg)
- Line: 804

### spi_engine_precompile_message
- Return type: static int
- Signature: spi_engine_precompile_message(struct spi_message * msg)
- Line: 304

### spi_engine_primary_lane_flag
- Return type: static void
- Signature: spi_engine_primary_lane_flag(struct spi_device * spi,u8 * rx_lane_flags,u8 * tx_lane_flags)
- Line: 182

### spi_engine_probe
- Return type: static int
- Signature: spi_engine_probe(struct platform_device * pdev)
- Line: 1104

### spi_engine_program_add_cmd
- Return type: static void
- Signature: spi_engine_program_add_cmd(struct spi_engine_program * p,bool dry,uint16_t cmd)
- Line: 201

### spi_engine_put_offload
- Return type: static void
- Signature: spi_engine_put_offload(struct spi_offload * offload)
- Line: 878

### spi_engine_read_rx_fifo
- Return type: static bool
- Signature: spi_engine_read_rx_fifo(struct spi_engine * spi_engine,struct spi_message * msg)
- Line: 616

### spi_engine_release_hw
- Return type: static void
- Signature: spi_engine_release_hw(void * p)
- Line: 1095

### spi_engine_rx_next
- Return type: static void
- Signature: spi_engine_rx_next(struct spi_message * msg)
- Line: 534

### spi_engine_rx_stream_request_dma_chan
- Return type: static dma_chan *
- Signature: spi_engine_rx_stream_request_dma_chan(struct spi_offload * offload)
- Line: 1078

### spi_engine_setup
- Return type: static int
- Signature: spi_engine_setup(struct spi_device * device)
- Line: 885

### spi_engine_transfer_one_message
- Return type: static int
- Signature: spi_engine_transfer_one_message(struct spi_controller * host,struct spi_message * msg)
- Line: 929

### spi_engine_trigger_disable
- Return type: static void
- Signature: spi_engine_trigger_disable(struct spi_offload * offload)
- Line: 1043

### spi_engine_trigger_enable
- Return type: static int
- Signature: spi_engine_trigger_enable(struct spi_offload * offload)
- Line: 999

### spi_engine_tx_next
- Return type: static void
- Signature: spi_engine_tx_next(struct spi_message * msg)
- Line: 516

### spi_engine_tx_stream_request_dma_chan
- Return type: static dma_chan *
- Signature: spi_engine_tx_stream_request_dma_chan(struct spi_offload * offload)
- Line: 1067

### spi_engine_unoptimize_message
- Return type: static int
- Signature: spi_engine_unoptimize_message(struct spi_message * msg)
- Line: 846

### spi_engine_write_cmd_fifo
- Return type: static bool
- Signature: spi_engine_write_cmd_fifo(struct spi_engine * spi_engine,struct spi_message * msg)
- Line: 552

### spi_engine_write_tx_fifo
- Return type: static bool
- Signature: spi_engine_write_tx_fifo(struct spi_engine * spi_engine,struct spi_message * msg)
- Line: 574

### spi_engine_xfer_next
- Return type: static void
- Signature: spi_engine_xfer_next(struct spi_message * msg,struct spi_transfer ** _xfer)
- Line: 499

## Structs (4)

### spi_engine
- Line: 162
- Members:
  - length: unsigned int
  - cmd_length: unsigned
  - cmd_buf: const uint16_t *
  - tx_xfer: spi_transfer *
  - tx_length: unsigned int
  - tx_buf: const uint8_t *
  - rx_xfer: spi_transfer *
  - rx_length: unsigned int
  - rx_buf: uint8_t *
  - spi_engine: spi_engine *
  - flags: unsigned long
  - offload_num: unsigned int
  - spi_mode_config: unsigned int
  - multi_lane_mode: unsigned int
  - rx_primary_lane_mask: u8
  - tx_primary_lane_mask: u8
  - rx_all_lanes_mask: u8
  - tx_all_lanes_mask: u8
  - bits_per_word: u8
  - clk: clk *
  - ref_clk: clk *
  - lock: spinlock_t
  - base: void __iomem *
  - msg_state: spi_engine_message_state
  - msg_complete: completion
  - int_enable: unsigned int
  - cs_inv: u8
  - offload_ctrl_mem_size: unsigned int
  - offload_sdo_mem_size: unsigned int
  - offload: spi_offload *
  - offload_caps: u32
  - offload_requires_sync: bool

### spi_engine_message_state
- Line: 125
- Members:
  - length: unsigned int
  - cmd_length: unsigned
  - cmd_buf: const uint16_t *
  - tx_xfer: spi_transfer *
  - tx_length: unsigned int
  - tx_buf: const uint8_t *
  - rx_xfer: spi_transfer *
  - rx_length: unsigned int
  - rx_buf: uint8_t *
  - spi_engine: spi_engine *
  - flags: unsigned long
  - offload_num: unsigned int
  - spi_mode_config: unsigned int
  - multi_lane_mode: unsigned int
  - rx_primary_lane_mask: u8
  - tx_primary_lane_mask: u8
  - rx_all_lanes_mask: u8
  - tx_all_lanes_mask: u8
  - bits_per_word: u8
  - clk: clk *
  - ref_clk: clk *
  - lock: spinlock_t
  - base: void __iomem *
  - msg_state: spi_engine_message_state
  - msg_complete: completion
  - int_enable: unsigned int
  - cs_inv: u8
  - offload_ctrl_mem_size: unsigned int
  - offload_sdo_mem_size: unsigned int
  - offload: spi_offload *
  - offload_caps: u32
  - offload_requires_sync: bool

### spi_engine_offload
- Line: 149
- Members:
  - length: unsigned int
  - cmd_length: unsigned
  - cmd_buf: const uint16_t *
  - tx_xfer: spi_transfer *
  - tx_length: unsigned int
  - tx_buf: const uint8_t *
  - rx_xfer: spi_transfer *
  - rx_length: unsigned int
  - rx_buf: uint8_t *
  - spi_engine: spi_engine *
  - flags: unsigned long
  - offload_num: unsigned int
  - spi_mode_config: unsigned int
  - multi_lane_mode: unsigned int
  - rx_primary_lane_mask: u8
  - tx_primary_lane_mask: u8
  - rx_all_lanes_mask: u8
  - tx_all_lanes_mask: u8
  - bits_per_word: u8
  - clk: clk *
  - ref_clk: clk *
  - lock: spinlock_t
  - base: void __iomem *
  - msg_state: spi_engine_message_state
  - msg_complete: completion
  - int_enable: unsigned int
  - cs_inv: u8
  - offload_ctrl_mem_size: unsigned int
  - offload_sdo_mem_size: unsigned int
  - offload: spi_offload *
  - offload_caps: u32
  - offload_requires_sync: bool

### spi_engine_program
- Line: 117
- Members:
  - length: unsigned int
  - cmd_length: unsigned
  - cmd_buf: const uint16_t *
  - tx_xfer: spi_transfer *
  - tx_length: unsigned int
  - tx_buf: const uint8_t *
  - rx_xfer: spi_transfer *
  - rx_length: unsigned int
  - rx_buf: uint8_t *
  - spi_engine: spi_engine *
  - flags: unsigned long
  - offload_num: unsigned int
  - spi_mode_config: unsigned int
  - multi_lane_mode: unsigned int
  - rx_primary_lane_mask: u8
  - tx_primary_lane_mask: u8
  - rx_all_lanes_mask: u8
  - tx_all_lanes_mask: u8
  - bits_per_word: u8
  - clk: clk *
  - ref_clk: clk *
  - lock: spinlock_t
  - base: void __iomem *
  - msg_state: spi_engine_message_state
  - msg_complete: completion
  - int_enable: unsigned int
  - cs_inv: u8
  - offload_ctrl_mem_size: unsigned int
  - offload_sdo_mem_size: unsigned int
  - offload: spi_offload *
  - offload_caps: u32
  - offload_requires_sync: bool

## Enums (1)

### __anon4728d0000103
- Line: 144

## Variables (3)

- static **spi_engine_driver** : platform_driver (line 1249)
- static **spi_engine_match_table** : const struct of_device_id[] (line 1243)
- static **spi_engine_offload_ops** : const struct spi_offload_ops (line 1088)

## Macros (61)

- **AXI_SPI_ENGINE_CUR_MSG_SYNC_ID** (line 91)
- **SPI_ENGINE_CMD**(inst,arg1,arg2) (line 93)
- **SPI_ENGINE_CMD_ASSERT**(delay,cs) (line 98)
- **SPI_ENGINE_CMD_CS_INV**(flags) (line 106)
- **SPI_ENGINE_CMD_REG_CLK_DIV** (line 78)
- **SPI_ENGINE_CMD_REG_CONFIG** (line 79)
- **SPI_ENGINE_CMD_REG_SDI_MASK** (line 81)
- **SPI_ENGINE_CMD_REG_SDO_MASK** (line 82)
- **SPI_ENGINE_CMD_REG_XFER_BITS** (line 80)
- **SPI_ENGINE_CMD_SLEEP**(delay) (line 102)
- **SPI_ENGINE_CMD_SYNC**(id) (line 104)
- **SPI_ENGINE_CMD_TRANSFER**(flags,n) (line 96)
- **SPI_ENGINE_CMD_WRITE**(reg,val) (line 100)
- **SPI_ENGINE_CONFIG_3WIRE** (line 69)
- **SPI_ENGINE_CONFIG_CPHA** (line 67)
- **SPI_ENGINE_CONFIG_CPOL** (line 68)
- **SPI_ENGINE_CONFIG_SDO_IDLE_HIGH** (line 70)
- **SPI_ENGINE_INST_ASSERT** (line 73)
- **SPI_ENGINE_INST_CS_INV** (line 76)
- **SPI_ENGINE_INST_MISC** (line 75)
- **SPI_ENGINE_INST_TRANSFER** (line 72)
- **SPI_ENGINE_INST_WRITE** (line 74)
- **SPI_ENGINE_INT_CMD_ALMOST_EMPTY** (line 59)
- **SPI_ENGINE_INT_OFFLOAD_SYNC** (line 63)
- **SPI_ENGINE_INT_SDI_ALMOST_FULL** (line 61)
- **SPI_ENGINE_INT_SDO_ALMOST_EMPTY** (line 60)
- **SPI_ENGINE_INT_SYNC** (line 62)
- **SPI_ENGINE_MAX_NUM_OFFLOADS** (line 48)
- **SPI_ENGINE_MISC_SLEEP** (line 85)
- **SPI_ENGINE_MISC_SYNC** (line 84)
- **SPI_ENGINE_MULTI_BUS_MODE_CONFLICTING** (line 115)
- **SPI_ENGINE_MULTI_BUS_MODE_UNKNOWN** (line 114)
- **SPI_ENGINE_OFFLOAD_CMD_FIFO_SIZE** (line 110)
- **SPI_ENGINE_OFFLOAD_CTRL_ENABLE** (line 65)
- **SPI_ENGINE_OFFLOAD_SDO_FIFO_SIZE** (line 111)
- **SPI_ENGINE_REG_CMD_FIFO** (line 43)
- **SPI_ENGINE_REG_CMD_FIFO_ROOM** (line 39)
- **SPI_ENGINE_REG_DATA_WIDTH** (line 26)
- **SPI_ENGINE_REG_DATA_WIDTH_MASK** (line 28)
- **SPI_ENGINE_REG_DATA_WIDTH_NUM_OF_SDIO_MASK** (line 27)
- **SPI_ENGINE_REG_INT_ENABLE** (line 32)
- **SPI_ENGINE_REG_INT_PENDING** (line 33)
- **SPI_ENGINE_REG_INT_SOURCE** (line 34)
- **SPI_ENGINE_REG_OFFLOAD_CMD_FIFO**(x) (line 53)
- **SPI_ENGINE_REG_OFFLOAD_CTRL**(x) (line 50)
- **SPI_ENGINE_REG_OFFLOAD_MEM_ADDR_WIDTH** (line 29)
- **SPI_ENGINE_REG_OFFLOAD_RESET**(x) (line 52)
- **SPI_ENGINE_REG_OFFLOAD_SDO_FIFO**(x) (line 54)
- **SPI_ENGINE_REG_OFFLOAD_STATUS**(x) (line 51)
- **SPI_ENGINE_REG_OFFLOAD_SYNC_ID** (line 37)
- **SPI_ENGINE_REG_RESET** (line 30)
- **SPI_ENGINE_REG_SDI_DATA_FIFO** (line 45)
- **SPI_ENGINE_REG_SDI_DATA_FIFO_PEEK** (line 46)
- **SPI_ENGINE_REG_SDI_FIFO_LEVEL** (line 41)
- **SPI_ENGINE_REG_SDO_DATA_FIFO** (line 44)
- **SPI_ENGINE_REG_SDO_FIFO_ROOM** (line 40)
- **SPI_ENGINE_REG_SYNC_ID** (line 36)
- **SPI_ENGINE_SPI_OFFLOAD_MEM_WIDTH_CMD** (line 57)
- **SPI_ENGINE_SPI_OFFLOAD_MEM_WIDTH_SDO** (line 56)
- **SPI_ENGINE_TRANSFER_READ** (line 88)
- **SPI_ENGINE_TRANSFER_WRITE** (line 87)
