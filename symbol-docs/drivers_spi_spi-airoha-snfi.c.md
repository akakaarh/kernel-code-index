# drivers/spi/spi-airoha-snfi.c

Subsystem: drivers/spi

## Functions (16)

### airoha_snand_dirmap_create
- Return type: static int
- Signature: airoha_snand_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 535

### airoha_snand_dirmap_read
- Return type: static ssize_t
- Signature: airoha_snand_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 555

### airoha_snand_dirmap_write
- Return type: static ssize_t
- Signature: airoha_snand_dirmap_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 748

### airoha_snand_exec_op
- Return type: static int
- Signature: airoha_snand_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 932

### airoha_snand_is_page_ops
- Return type: static bool
- Signature: airoha_snand_is_page_ops(const struct spi_mem_op * op)
- Line: 486

### airoha_snand_nfi_init
- Return type: static int
- Signature: airoha_snand_nfi_init(struct airoha_snand_ctrl * as_ctrl)
- Line: 471

### airoha_snand_probe
- Return type: static int
- Signature: airoha_snand_probe(struct platform_device * pdev)
- Line: 1060

### airoha_snand_read_data
- Return type: static int
- Signature: airoha_snand_read_data(struct airoha_snand_ctrl * as_ctrl,u8 * data,int len,int buswidth)
- Line: 433

### airoha_snand_read_data_from_fifo
- Return type: static int
- Signature: airoha_snand_read_data_from_fifo(struct airoha_snand_ctrl * as_ctrl,u8 * ptr,int len)
- Line: 299

### airoha_snand_set_cs
- Return type: static int
- Signature: airoha_snand_set_cs(struct airoha_snand_ctrl * as_ctrl,u8 cs)
- Line: 258

### airoha_snand_set_fifo_op
- Return type: static int
- Signature: airoha_snand_set_fifo_op(struct airoha_snand_ctrl * as_ctrl,u8 op_cmd,int op_len)
- Line: 228

### airoha_snand_set_mode
- Return type: static int
- Signature: airoha_snand_set_mode(struct airoha_snand_ctrl * as_ctrl,enum airoha_snand_mode mode)
- Line: 333

### airoha_snand_setup
- Return type: static int
- Signature: airoha_snand_setup(struct spi_device * spi)
- Line: 1021

### airoha_snand_supports_op
- Return type: static bool
- Signature: airoha_snand_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 518

### airoha_snand_write_data
- Return type: static int
- Signature: airoha_snand_write_data(struct airoha_snand_ctrl * as_ctrl,const u8 * data,int len,int buswidth)
- Line: 395

### airoha_snand_write_data_to_fifo
- Return type: static int
- Signature: airoha_snand_write_data_to_fifo(struct airoha_snand_ctrl * as_ctrl,const u8 * data,int len)
- Line: 263

## Structs (1)

### airoha_snand_ctrl
- Line: 221
- Members:
  - dev: device *
  - regmap_ctrl: regmap *
  - regmap_nfi: regmap *
  - spi_clk: clk *

## Enums (2)

### airoha_snand_cs
- Line: 216

### airoha_snand_mode
- Line: 210

## Variables (6)

- static **airoha_snand_driver** : platform_driver (line 1135)
- static **airoha_snand_ids** : const struct of_device_id[] (line 1054)
- static **airoha_snand_mem_ops** : const struct spi_controller_mem_ops (line 1008)
- static **airoha_snand_nodma_mem_ops** : const struct spi_controller_mem_ops (line 1016)
- static **spi_ctrl_regmap_config** : const struct regmap_config (line 1038)
- static **spi_nfi_regmap_config** : const struct regmap_config (line 1046)

## Macros (135)

- **REG_SPI_CTRL_BASE** (line 29)
- **REG_SPI_CTRL_CSHEXT** (line 34)
- **REG_SPI_CTRL_CSLEXT** (line 35)
- **REG_SPI_CTRL_DFIFO_EMPTY** (line 67)
- **REG_SPI_CTRL_DFIFO_FULL** (line 61)
- **REG_SPI_CTRL_DFIFO_RD** (line 70)
- **REG_SPI_CTRL_DFIFO_RDATA** (line 73)
- **REG_SPI_CTRL_DFIFO_WDATA** (line 64)
- **REG_SPI_CTRL_DUMMY** (line 76)
- **REG_SPI_CTRL_INTERRUPT** (line 80)
- **REG_SPI_CTRL_INTERRUPT_EN** (line 81)
- **REG_SPI_CTRL_MACMUX_SEL** (line 43)
- **REG_SPI_CTRL_MANUAL_EN** (line 45)
- **REG_SPI_CTRL_MTX_MODE_TOG** (line 37)
- **REG_SPI_CTRL_NFI2SPI_EN** (line 87)
- **REG_SPI_CTRL_OPFIFO_EMPTY** (line 48)
- **REG_SPI_CTRL_OPFIFO_FULL** (line 55)
- **REG_SPI_CTRL_OPFIFO_WDATA** (line 51)
- **REG_SPI_CTRL_OPFIFO_WR** (line 58)
- **REG_SPI_CTRL_PROBE_SEL** (line 79)
- **REG_SPI_CTRL_RDCTL_FSM** (line 40)
- **REG_SPI_CTRL_READ_IDLE_EN** (line 32)
- **REG_SPI_CTRL_READ_MODE** (line 31)
- **REG_SPI_CTRL_SFC_STRAP** (line 85)
- **REG_SPI_CTRL_SIDLY** (line 33)
- **REG_SPI_CTRL_SI_CK_SEL** (line 82)
- **REG_SPI_CTRL_SW_CFGNANDADDR_EN** (line 84)
- **REG_SPI_CTRL_SW_CFGNANDADDR_VAL** (line 83)
- **REG_SPI_NFI_ADDR_NOB** (line 129)
- **REG_SPI_NFI_CMD** (line 127)
- **REG_SPI_NFI_CNFG** (line 91)
- **REG_SPI_NFI_CON** (line 103)
- **REG_SPI_NFI_FDM0L** (line 135)
- **REG_SPI_NFI_FDM0M** (line 136)
- **REG_SPI_NFI_FDM7L** (line 137)
- **REG_SPI_NFI_FDM7M** (line 138)
- **REG_SPI_NFI_FIFODATA0** (line 139)
- **REG_SPI_NFI_FIFODATA1** (line 140)
- **REG_SPI_NFI_FIFODATA2** (line 141)
- **REG_SPI_NFI_FIFODATA3** (line 142)
- **REG_SPI_NFI_FIFOSTA** (line 133)
- **REG_SPI_NFI_INTR** (line 124)
- **REG_SPI_NFI_INTR_EN** (line 110)
- **REG_SPI_NFI_MASTERSTA** (line 143)
- **REG_SPI_NFI_NOR_PROG_ADDR** (line 158)
- **REG_SPI_NFI_NOR_RD_ADDR** (line 159)
- **REG_SPI_NFI_PAGEFMT** (line 99)
- **REG_SPI_NFI_PG_CTL1** (line 154)
- **REG_SPI_NFI_PG_CTL2** (line 157)
- **REG_SPI_NFI_RD_CTL2** (line 149)
- **REG_SPI_NFI_RD_CTL3** (line 152)
- **REG_SPI_NFI_SECCUS_SIZE** (line 145)
- **REG_SPI_NFI_SNF_MISC_CTL** (line 161)
- **REG_SPI_NFI_SNF_MISC_CTL2** (line 164)
- **REG_SPI_NFI_SNF_NFI_CNFG** (line 174)
- **REG_SPI_NFI_SNF_STA_CTL1** (line 168)
- **REG_SPI_NFI_SNF_STA_CTL2** (line 172)
- **REG_SPI_NFI_STA** (line 132)
- **REG_SPI_NFI_STRADDR** (line 134)
- **SNAND_FIFO_RX_BUSWIDTH_DUAL** (line 204)
- **SNAND_FIFO_RX_BUSWIDTH_QUAD** (line 205)
- **SNAND_FIFO_RX_BUSWIDTH_SINGLE** (line 203)
- **SNAND_FIFO_TX_BUSWIDTH_DUAL** (line 201)
- **SNAND_FIFO_TX_BUSWIDTH_QUAD** (line 202)
- **SNAND_FIFO_TX_BUSWIDTH_SINGLE** (line 200)
- **SPI_CTRL_CTRL_DUMMY** (line 77)
- **SPI_CTRL_DFIFO_EMPTY** (line 68)
- **SPI_CTRL_DFIFO_FULL** (line 62)
- **SPI_CTRL_DFIFO_RD** (line 71)
- **SPI_CTRL_DFIFO_RDATA** (line 74)
- **SPI_CTRL_DFIFO_WDATA** (line 65)
- **SPI_CTRL_MANUAL_EN** (line 46)
- **SPI_CTRL_MTX_MODE_TOG** (line 38)
- **SPI_CTRL_NFI2SPI_EN** (line 88)
- **SPI_CTRL_OPFIFO_EMPTY** (line 49)
- **SPI_CTRL_OPFIFO_FULL** (line 56)
- **SPI_CTRL_OPFIFO_LEN** (line 52)
- **SPI_CTRL_OPFIFO_OP** (line 53)
- **SPI_CTRL_OPFIFO_WR** (line 59)
- **SPI_CTRL_RDCTL_FSM** (line 41)
- **SPI_MAX_TRANSFER_SIZE** (line 208)
- **SPI_NAND_CACHE_SIZE** (line 207)
- **SPI_NAND_OP_BLOCK_ERASE** (line 195)
- **SPI_NAND_OP_DIE_SELECT** (line 197)
- **SPI_NAND_OP_GET_FEATURE** (line 178)
- **SPI_NAND_OP_PAGE_READ** (line 180)
- **SPI_NAND_OP_PROGRAM_EXECUTE** (line 193)
- **SPI_NAND_OP_PROGRAM_LOAD_QUAD** (line 190)
- **SPI_NAND_OP_PROGRAM_LOAD_RAMDOM_SINGLE** (line 191)
- **SPI_NAND_OP_PROGRAM_LOAD_RAMDON_QUAD** (line 192)
- **SPI_NAND_OP_PROGRAM_LOAD_SINGLE** (line 189)
- **SPI_NAND_OP_READ_FROM_CACHE_DUAL** (line 183)
- **SPI_NAND_OP_READ_FROM_CACHE_DUALIO** (line 184)
- **SPI_NAND_OP_READ_FROM_CACHE_QUAD** (line 185)
- **SPI_NAND_OP_READ_FROM_CACHE_QUADIO** (line 186)
- **SPI_NAND_OP_READ_FROM_CACHE_SINGLE** (line 181)
- **SPI_NAND_OP_READ_FROM_CACHE_SINGLE_FAST** (line 182)
- **SPI_NAND_OP_READ_ID** (line 194)
- **SPI_NAND_OP_RESET** (line 196)
- **SPI_NAND_OP_SET_FEATURE** (line 179)
- **SPI_NAND_OP_WRITE_DISABLE** (line 188)
- **SPI_NAND_OP_WRITE_ENABLE** (line 187)
- **SPI_NFI_ACCESS_LOCK_EN** (line 116)
- **SPI_NFI_AHB_DONE** (line 125)
- **SPI_NFI_AHB_DONE_EN** (line 117)
- **SPI_NFI_ALL_IRQ_EN** (line 118)
- **SPI_NFI_AUTO_FDM_EN** (line 96)
- **SPI_NFI_BUSY_RETURN_EN** (line 115)
- **SPI_NFI_CUS_SEC_SIZE** (line 146)
- **SPI_NFI_CUS_SEC_SIZE_EN** (line 147)
- **SPI_NFI_DATA_READ_CMD** (line 150)
- **SPI_NFI_DATA_READ_WR_MODE** (line 162)
- **SPI_NFI_DMA_BURST_EN** (line 94)
- **SPI_NFI_DMA_MODE** (line 92)
- **SPI_NFI_ERASE_DONE_EN** (line 114)
- **SPI_NFI_FIFO_FLUSH** (line 104)
- **SPI_NFI_HW_ECC_EN** (line 95)
- **SPI_NFI_LOAD_TO_CACHE_DONE** (line 170)
- **SPI_NFI_OPMODE** (line 97)
- **SPI_NFI_PAGE_SIZE** (line 100)
- **SPI_NFI_PG_LOAD_CMD** (line 155)
- **SPI_NFI_PROG_LOAD_BYTE_NUM** (line 166)
- **SPI_NFI_RD_DONE_EN** (line 111)
- **SPI_NFI_RD_TRIG** (line 106)
- **SPI_NFI_READ_DATA_BYTE_NUM** (line 165)
- **SPI_NFI_READ_FROM_CACHE_DONE** (line 169)
- **SPI_NFI_READ_MODE** (line 93)
- **SPI_NFI_ROW_ADDR_NOB** (line 130)
- **SPI_NFI_RST** (line 105)
- **SPI_NFI_RST_DONE_EN** (line 113)
- **SPI_NFI_SEC_NUM** (line 108)
- **SPI_NFI_SPARE_SIZE** (line 101)
- **SPI_NFI_SPI_MODE** (line 175)
- **SPI_NFI_WR_DONE_EN** (line 112)
- **SPI_NFI_WR_TRIG** (line 107)
