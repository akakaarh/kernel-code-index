# drivers/spi/spi-sg2044-nor.c

Subsystem: drivers/spi

## Functions (12)

### sg2044_spifmc_exec_op
- Return type: static int
- Signature: sg2044_spifmc_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 388

### sg2044_spifmc_init
- Return type: static void
- Signature: sg2044_spifmc_init(struct sg2044_spifmc * spifmc)
- Line: 411

### sg2044_spifmc_init_reg
- Return type: static u32
- Signature: sg2044_spifmc_init_reg(struct sg2044_spifmc * spifmc)
- Line: 119

### sg2044_spifmc_probe
- Return type: static int
- Signature: sg2044_spifmc_probe(struct platform_device * pdev)
- Line: 433

### sg2044_spifmc_read
- Return type: static ssize_t
- Signature: sg2044_spifmc_read(struct sg2044_spifmc * spifmc,const struct spi_mem_op * op)
- Line: 193

### sg2044_spifmc_read_64k
- Return type: static ssize_t
- Signature: sg2044_spifmc_read_64k(struct sg2044_spifmc * spifmc,const struct spi_mem_op * op,loff_t from,size_t len,u_char * buf)
- Line: 137

### sg2044_spifmc_tran_cmd
- Return type: static ssize_t
- Signature: sg2044_spifmc_tran_cmd(struct sg2044_spifmc * spifmc,const struct spi_mem_op * op)
- Line: 277

### sg2044_spifmc_trans
- Return type: static void
- Signature: sg2044_spifmc_trans(struct sg2044_spifmc * spifmc,const struct spi_mem_op * op)
- Line: 310

### sg2044_spifmc_trans_reg
- Return type: static ssize_t
- Signature: sg2044_spifmc_trans_reg(struct sg2044_spifmc * spifmc,const struct spi_mem_op * op)
- Line: 321

### sg2044_spifmc_wait_int
- Return type: static int
- Signature: sg2044_spifmc_wait_int(struct sg2044_spifmc * spifmc,u8 int_type)
- Line: 102

### sg2044_spifmc_wait_xfer_size
- Return type: static int
- Signature: sg2044_spifmc_wait_xfer_size(struct sg2044_spifmc * spifmc,int xfer_size)
- Line: 110

### sg2044_spifmc_write
- Return type: static ssize_t
- Signature: sg2044_spifmc_write(struct sg2044_spifmc * spifmc,const struct spi_mem_op * op)
- Line: 219

## Structs (2)

### sg2044_spifmc
- Line: 93
- Members:
  - has_opt_reg: bool
  - rd_fifo_int_trigger_level: u32
  - ctrl: spi_controller *
  - io_base: void __iomem *
  - dev: device *
  - lock: mutex
  - clk: clk *
  - chip_info: const struct sg204x_spifmc_chip_info *

### sg204x_spifmc_chip_info
- Line: 88
- Members:
  - has_opt_reg: bool
  - rd_fifo_int_trigger_level: u32
  - ctrl: spi_controller *
  - io_base: void __iomem *
  - dev: device *
  - lock: mutex
  - clk: clk *
  - chip_info: const struct sg204x_spifmc_chip_info *

## Variables (5)

- static **sg2042_chip_info** : const struct sg204x_spifmc_chip_info (line 487)
- static **sg2044_chip_info** : const struct sg204x_spifmc_chip_info (line 482)
- static **sg2044_nor_driver** : platform_driver (line 499)
- static **sg2044_spifmc_match** : const struct of_device_id[] (line 492)
- static **sg2044_spifmc_mem_ops** : const struct spi_controller_mem_ops (line 407)

## Macros (60)

- **SPIFMC_CE_CTRL** (line 28)
- **SPIFMC_CE_CTRL_CEMANUAL** (line 29)
- **SPIFMC_CE_CTRL_CEMANUAL_EN** (line 30)
- **SPIFMC_CTRL** (line 17)
- **SPIFMC_CTRL_CET** (line 36)
- **SPIFMC_CTRL_CET_MASK** (line 35)
- **SPIFMC_CTRL_CPHA** (line 18)
- **SPIFMC_CTRL_CPOL** (line 19)
- **SPIFMC_CTRL_FM_INTVL** (line 34)
- **SPIFMC_CTRL_FM_INTVL_MASK** (line 33)
- **SPIFMC_CTRL_FRAME_LEN_SHIFT** (line 25)
- **SPIFMC_CTRL_HOLD_OL** (line 20)
- **SPIFMC_CTRL_LSBF** (line 22)
- **SPIFMC_CTRL_SCK_DIV_MASK** (line 26)
- **SPIFMC_CTRL_SCK_DIV_SHIFT** (line 24)
- **SPIFMC_CTRL_SRST** (line 23)
- **SPIFMC_CTRL_WP_OL** (line 21)
- **SPIFMC_DLY_CTRL** (line 32)
- **SPIFMC_DMMR** (line 38)
- **SPIFMC_FIFO_PORT** (line 64)
- **SPIFMC_FIFO_PT** (line 65)
- **SPIFMC_INT_EN** (line 74)
- **SPIFMC_INT_RD_FIFO** (line 69)
- **SPIFMC_INT_RD_FIFO_EN** (line 76)
- **SPIFMC_INT_RX_FRAME** (line 71)
- **SPIFMC_INT_RX_FRAME_EN** (line 78)
- **SPIFMC_INT_STS** (line 67)
- **SPIFMC_INT_TRAN_DONE** (line 68)
- **SPIFMC_INT_TRAN_DONE_EN** (line 75)
- **SPIFMC_INT_TX_FRAME** (line 72)
- **SPIFMC_INT_TX_FRAME_EN** (line 79)
- **SPIFMC_INT_WR_FIFO** (line 70)
- **SPIFMC_INT_WR_FIFO_EN** (line 77)
- **SPIFMC_MAX_FIFO_DEPTH** (line 84)
- **SPIFMC_MAX_READ_SIZE** (line 86)
- **SPIFMC_OPT** (line 81)
- **SPIFMC_OPT_DISABLE_FIFO_FLUSH** (line 82)
- **SPIFMC_TRAN_CSR** (line 40)
- **SPIFMC_TRAN_CSR_ADDR4B_SHIFT** (line 60)
- **SPIFMC_TRAN_CSR_ADDR_BYTES_MASK** (line 51)
- **SPIFMC_TRAN_CSR_ADDR_BYTES_SHIFT** (line 52)
- **SPIFMC_TRAN_CSR_BUS_WIDTH_1_BIT** (line 46)
- **SPIFMC_TRAN_CSR_BUS_WIDTH_2_BIT** (line 47)
- **SPIFMC_TRAN_CSR_BUS_WIDTH_4_BIT** (line 48)
- **SPIFMC_TRAN_CSR_BUS_WIDTH_MASK** (line 45)
- **SPIFMC_TRAN_CSR_CMD4B_SHIFT** (line 61)
- **SPIFMC_TRAN_CSR_DMA_EN** (line 49)
- **SPIFMC_TRAN_CSR_FAST_MODE** (line 44)
- **SPIFMC_TRAN_CSR_FIFO_TRG_LVL_1_BYTE** (line 55)
- **SPIFMC_TRAN_CSR_FIFO_TRG_LVL_2_BYTE** (line 56)
- **SPIFMC_TRAN_CSR_FIFO_TRG_LVL_4_BYTE** (line 57)
- **SPIFMC_TRAN_CSR_FIFO_TRG_LVL_8_BYTE** (line 58)
- **SPIFMC_TRAN_CSR_FIFO_TRG_LVL_MASK** (line 54)
- **SPIFMC_TRAN_CSR_GO_BUSY** (line 59)
- **SPIFMC_TRAN_CSR_MISO_LEVEL** (line 50)
- **SPIFMC_TRAN_CSR_TRAN_MODE_MASK** (line 41)
- **SPIFMC_TRAN_CSR_TRAN_MODE_RX** (line 42)
- **SPIFMC_TRAN_CSR_TRAN_MODE_TX** (line 43)
- **SPIFMC_TRAN_CSR_WITH_CMD** (line 53)
- **SPIFMC_TRAN_NUM** (line 63)
