# drivers/spi/spi-pic32-sqi.c

Subsystem: drivers/spi

## Functions (18)

### pic32_clrbits
- Return type: static void
- Signature: pic32_clrbits(void __iomem * reg,u32 clr)
- Line: 160

### pic32_setbits
- Return type: static void
- Signature: pic32_setbits(void __iomem * reg,u32 set)
- Line: 155

### pic32_sqi_can_dma
- Return type: static bool
- Signature: pic32_sqi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * x)
- Line: 331

### pic32_sqi_disable_int
- Return type: static void
- Signature: pic32_sqi_disable_int(struct pic32_sqi * sqi)
- Line: 193

### pic32_sqi_enable_int
- Return type: static void
- Signature: pic32_sqi_enable_int(struct pic32_sqi * sqi)
- Line: 184

### pic32_sqi_hw_init
- Return type: static void
- Signature: pic32_sqi_hw_init(struct pic32_sqi * sqi)
- Line: 507

### pic32_sqi_isr
- Return type: static irqreturn_t
- Signature: pic32_sqi_isr(int irq,void * dev_id)
- Line: 199

### pic32_sqi_one_message
- Return type: static int
- Signature: pic32_sqi_one_message(struct spi_controller * host,struct spi_message * msg)
- Line: 339

### pic32_sqi_one_transfer
- Return type: static int
- Signature: pic32_sqi_one_transfer(struct pic32_sqi * sqi,struct spi_message * mesg,struct spi_transfer * xfer)
- Line: 257

### pic32_sqi_prepare_hardware
- Return type: static int
- Signature: pic32_sqi_prepare_hardware(struct spi_controller * host)
- Line: 319

### pic32_sqi_probe
- Return type: static int
- Signature: pic32_sqi_probe(struct platform_device * pdev)
- Line: 569

### pic32_sqi_remove
- Return type: static void
- Signature: pic32_sqi_remove(struct platform_device * pdev)
- Line: 664

### pic32_sqi_set_clk_rate
- Return type: static int
- Signature: pic32_sqi_set_clk_rate(struct pic32_sqi * sqi,u32 sck)
- Line: 165

### pic32_sqi_unprepare_hardware
- Return type: static int
- Signature: pic32_sqi_unprepare_hardware(struct spi_controller * host)
- Line: 442

### ring_desc_get
- Return type: static ring_desc *
- Signature: ring_desc_get(struct pic32_sqi * sqi)
- Line: 240

### ring_desc_put
- Return type: static void
- Signature: ring_desc_put(struct pic32_sqi * sqi,struct ring_desc * rdesc)
- Line: 252

### ring_desc_ring_alloc
- Return type: static int
- Signature: ring_desc_ring_alloc(struct pic32_sqi * sqi)
- Line: 454

### ring_desc_ring_free
- Return type: static void
- Signature: ring_desc_ring_free(struct pic32_sqi * sqi)
- Line: 499

## Structs (3)

### buf_desc
- Line: 97
- Members:
  - bd_ctrl: u32
  - bd_status: u32
  - bd_addr: u32
  - bd_nextp: u32
  - list: list_head
  - bd: buf_desc *
  - bd_dma: dma_addr_t
  - xfer_len: u32
  - regs: void __iomem *
  - sys_clk: clk *
  - base_clk: clk *
  - host: spi_controller *
  - irq: int
  - xfer_done: completion
  - ring: ring_desc *
  - bd: void *
  - bd_dma: dma_addr_t
  - bd_list_free: list_head
  - bd_list_used: list_head
  - cur_spi: spi_device *
  - cur_speed: u32
  - cur_mode: u8

### pic32_sqi
- Line: 138
- Members:
  - bd_ctrl: u32
  - bd_status: u32
  - bd_addr: u32
  - bd_nextp: u32
  - list: list_head
  - bd: buf_desc *
  - bd_dma: dma_addr_t
  - xfer_len: u32
  - regs: void __iomem *
  - sys_clk: clk *
  - base_clk: clk *
  - host: spi_controller *
  - irq: int
  - xfer_done: completion
  - ring: ring_desc *
  - bd: void *
  - bd_dma: dma_addr_t
  - bd_list_free: list_head
  - bd_list_used: list_head
  - cur_spi: spi_device *
  - cur_speed: u32
  - cur_mode: u8

### ring_desc
- Line: 127
- Members:
  - bd_ctrl: u32
  - bd_status: u32
  - bd_addr: u32
  - bd_nextp: u32
  - list: list_head
  - bd: buf_desc *
  - bd_dma: dma_addr_t
  - xfer_len: u32
  - regs: void __iomem *
  - sys_clk: clk *
  - base_clk: clk *
  - host: spi_controller *
  - irq: int
  - xfer_done: completion
  - ring: ring_desc *
  - bd: void *
  - bd_dma: dma_addr_t
  - bd_list_free: list_head
  - bd_list_used: list_head
  - cur_spi: spi_device *
  - cur_speed: u32
  - cur_mode: u8

## Variables (2)

- static **pic32_sqi_driver** : platform_driver (line 685)
- static **pic32_sqi_of_ids** : const struct of_device_id[] (line 679)

## Macros (80)

- **BD_BUFLEN** (line 105)
- **BD_CBD_INT_EN** (line 106)
- **BD_CS_DEASSERT** (line 117)
- **BD_DATA_RECV** (line 110)
- **BD_DDR** (line 111)
- **BD_DEVSEL_SHIFT** (line 116)
- **BD_DUAL** (line 112)
- **BD_EN** (line 118)
- **BD_LAST** (line 109)
- **BD_LIFM** (line 108)
- **BD_LSBF** (line 114)
- **BD_PKT_INT_EN** (line 107)
- **BD_QUAD** (line 113)
- **BD_STAT_CHECK** (line 115)
- **PESQI_BDDONE** (line 87)
- **PESQI_BDP_START** (line 94)
- **PESQI_BD_BASE_ADDR_REG** (line 36)
- **PESQI_BD_BUF_LEN_MAX** (line 135)
- **PESQI_BD_COUNT** (line 136)
- **PESQI_BD_CTRL_REG** (line 34)
- **PESQI_BD_CUR_ADDR_REG** (line 35)
- **PESQI_BD_POLL_CTRL_REG** (line 38)
- **PESQI_BD_RX_DMA_STAT_REG** (line 40)
- **PESQI_BD_STAT_REG** (line 37)
- **PESQI_BD_TX_DMA_STAT_REG** (line 39)
- **PESQI_BURST_EN** (line 58)
- **PESQI_CLKDIV** (line 72)
- **PESQI_CLKDIV_SHIFT** (line 71)
- **PESQI_CLK_CTRL_REG** (line 25)
- **PESQI_CLK_EN** (line 69)
- **PESQI_CLK_STABLE** (line 70)
- **PESQI_CMD_THRES_REG** (line 26)
- **PESQI_CONF_REG** (line 23)
- **PESQI_CPHA** (line 51)
- **PESQI_CPOL** (line 52)
- **PESQI_CSEN_SHIFT** (line 65)
- **PESQI_CS_CTRL_HW** (line 59)
- **PESQI_CTRL_REG** (line 24)
- **PESQI_DMAERR** (line 89)
- **PESQI_DMA_EN** (line 92)
- **PESQI_DUAL_LANE** (line 63)
- **PESQI_EN** (line 66)
- **PESQI_HOLD_EN** (line 57)
- **PESQI_INT_ENABLE_REG** (line 28)
- **PESQI_INT_SIGEN_REG** (line 42)
- **PESQI_INT_STAT_REG** (line 29)
- **PESQI_INT_THRES_REG** (line 27)
- **PESQI_LANES_SHIFT** (line 61)
- **PESQI_LSBF** (line 53)
- **PESQI_MODE** (line 45)
- **PESQI_MODE_BOOT** (line 46)
- **PESQI_MODE_DMA** (line 48)
- **PESQI_MODE_PIO** (line 47)
- **PESQI_MODE_SHIFT** (line 50)
- **PESQI_MODE_XIP** (line 49)
- **PESQI_PKTCOMP** (line 88)
- **PESQI_POLL_EN** (line 93)
- **PESQI_QUAD_LANE** (line 64)
- **PESQI_RXEMPTY** (line 84)
- **PESQI_RXFULL** (line 85)
- **PESQI_RXLATCH** (line 54)
- **PESQI_RXTHR** (line 86)
- **PESQI_RXTHR_MASK** (line 77)
- **PESQI_RXTHR_SHIFT** (line 78)
- **PESQI_RX_DATA_REG** (line 31)
- **PESQI_SERMODE** (line 55)
- **PESQI_SINGLE_LANE** (line 62)
- **PESQI_SOFT_RESET** (line 60)
- **PESQI_STAT1_REG** (line 32)
- **PESQI_STAT2_REG** (line 33)
- **PESQI_THRES_REG** (line 41)
- **PESQI_TXEMPTY** (line 81)
- **PESQI_TXFULL** (line 82)
- **PESQI_TXTHR** (line 83)
- **PESQI_TXTHR_MASK** (line 75)
- **PESQI_TXTHR_SHIFT** (line 76)
- **PESQI_TX_DATA_REG** (line 30)
- **PESQI_WP_EN** (line 56)
- **PESQI_XIP_CONF1_REG** (line 21)
- **PESQI_XIP_CONF2_REG** (line 22)
