# drivers/spi/spi-amd.c

Subsystem: drivers/spi

## Functions (38)

### amd_is_spi_read_cmd
- Return type: static bool
- Signature: amd_is_spi_read_cmd(const u16 op)
- Line: 414

### amd_is_spi_read_cmd_4b
- Return type: static bool
- Signature: amd_is_spi_read_cmd_4b(const u16 op)
- Line: 400

### amd_is_spi_write_cmd
- Return type: static bool
- Signature: amd_is_spi_write_cmd(const u16 op)
- Line: 429

### amd_set_spi_addr_mode
- Return type: static void
- Signature: amd_set_spi_addr_mode(struct amd_spi * amd_spi,const struct spi_mem_op * op)
- Line: 722

### amd_set_spi_freq
- Return type: static void
- Signature: amd_set_spi_freq(struct amd_spi * amd_spi,u32 speed_hz)
- Line: 282

### amd_spi_adjust_op_size
- Return type: static int
- Signature: amd_spi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 476

### amd_spi_busy_wait
- Return type: static int
- Signature: amd_spi_busy_wait(struct amd_spi * amd_spi)
- Line: 215

### amd_spi_clear_chip
- Return type: static void
- Signature: amd_spi_clear_chip(struct amd_spi * amd_spi,u8 chip_select)
- Line: 179

### amd_spi_clear_fifo_ptr
- Return type: static void
- Signature: amd_spi_clear_fifo_ptr(struct amd_spi * amd_spi)
- Line: 184

### amd_spi_exec_mem_op
- Return type: static int
- Signature: amd_spi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 733

### amd_spi_execute_opcode
- Return type: static int
- Signature: amd_spi_execute_opcode(struct amd_spi * amd_spi)
- Line: 236

### amd_spi_fifo_xfer
- Return type: static int
- Signature: amd_spi_fifo_xfer(struct amd_spi * amd_spi,struct spi_controller * host,struct spi_message * message)
- Line: 312

### amd_spi_hiddma_read
- Return type: static void
- Signature: amd_spi_hiddma_read(struct amd_spi * amd_spi,const struct spi_mem_op * op)
- Line: 603

### amd_spi_hiddma_write
- Return type: static void
- Signature: amd_spi_hiddma_write(struct amd_spi * amd_spi,const struct spi_mem_op * op)
- Line: 511

### amd_spi_host_setup
- Return type: static int
- Signature: amd_spi_host_setup(struct spi_device * spi)
- Line: 261

### amd_spi_host_transfer
- Return type: static int
- Signature: amd_spi_host_transfer(struct spi_controller * host,struct spi_message * msg)
- Line: 771

### amd_spi_max_transfer_size
- Return type: static size_t
- Signature: amd_spi_max_transfer_size(struct spi_device * spi)
- Line: 786

### amd_spi_mem_data_in
- Return type: static void
- Signature: amd_spi_mem_data_in(struct amd_spi * amd_spi,const struct spi_mem_op * op)
- Line: 661

### amd_spi_mem_data_out
- Return type: static void
- Signature: amd_spi_mem_data_out(struct amd_spi * amd_spi,const struct spi_mem_op * op)
- Line: 541

### amd_spi_probe
- Return type: static int
- Signature: amd_spi_probe(struct platform_device * pdev)
- Line: 851

### amd_spi_probe_common
- Return type: int
- Signature: amd_spi_probe_common(struct device * dev,struct spi_controller * host)
- Line: 821

### amd_spi_readreg16
- Return type: static u16
- Signature: amd_spi_readreg16(struct amd_spi * amd_spi,int idx)
- Line: 136

### amd_spi_readreg32
- Return type: static u32
- Signature: amd_spi_readreg32(struct amd_spi * amd_spi,int idx)
- Line: 146

### amd_spi_readreg64
- Return type: static u64
- Signature: amd_spi_readreg64(struct amd_spi * amd_spi,int idx)
- Line: 156

### amd_spi_readreg8
- Return type: static u8
- Signature: amd_spi_readreg8(struct amd_spi * amd_spi,int idx)
- Line: 118

### amd_spi_select_chip
- Return type: static void
- Signature: amd_spi_select_chip(struct amd_spi * amd_spi,u8 cs)
- Line: 174

### amd_spi_set_addr
- Return type: static void
- Signature: amd_spi_set_addr(struct amd_spi * amd_spi,const struct spi_mem_op * op)
- Line: 495

### amd_spi_set_opcode
- Return type: static int
- Signature: amd_spi_set_opcode(struct amd_spi * amd_spi,u8 cmd_opcode)
- Line: 189

### amd_spi_set_rx_count
- Return type: static void
- Signature: amd_spi_set_rx_count(struct amd_spi * amd_spi,u8 rx_count)
- Line: 205

### amd_spi_set_tx_count
- Return type: static void
- Signature: amd_spi_set_tx_count(struct amd_spi * amd_spi,u8 tx_count)
- Line: 210

### amd_spi_setclear_reg32
- Return type: static void
- Signature: amd_spi_setclear_reg32(struct amd_spi * amd_spi,int idx,u32 set,u32 clear)
- Line: 166

### amd_spi_setclear_reg8
- Return type: static void
- Signature: amd_spi_setclear_reg8(struct amd_spi * amd_spi,int idx,u8 set,u8 clear)
- Line: 128

### amd_spi_setup_hiddma
- Return type: static int
- Signature: amd_spi_setup_hiddma(struct amd_spi * amd_spi,struct device * dev)
- Line: 791

### amd_spi_supports_op
- Return type: static bool
- Signature: amd_spi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 440

### amd_spi_writereg16
- Return type: static void
- Signature: amd_spi_writereg16(struct amd_spi * amd_spi,int idx,u16 val)
- Line: 141

### amd_spi_writereg32
- Return type: static void
- Signature: amd_spi_writereg32(struct amd_spi * amd_spi,int idx,u32 val)
- Line: 151

### amd_spi_writereg64
- Return type: static void
- Signature: amd_spi_writereg64(struct amd_spi * amd_spi,int idx,u64 val)
- Line: 161

### amd_spi_writereg8
- Return type: static void
- Signature: amd_spi_writereg8(struct amd_spi * amd_spi,int idx,u8 val)
- Line: 123

## Structs (1)

### amd_spi_freq
- Line: 112
- Members:
  - speed_hz: u32
  - enable_val: u32
  - spd7_val: u32

## Enums (1)

### amd_spi_speed
- Line: 93

## Variables (5)

- static **amd_spi_driver** : platform_driver (line 886)
- static **amd_spi_freq** : const struct amd_spi_freq[] (line 270)
- static **amd_spi_mem_caps** : const struct spi_controller_mem_caps (line 767)
- static **amd_spi_mem_ops** : const struct spi_controller_mem_ops (line 761)
- static **spi_acpi_match** : const struct acpi_device_id[] (line 877)

## Macros (55)

- **AMD_SPI_ADDR32CTRL_REG** (line 40)
- **AMD_SPI_ALT_CS_MASK** (line 34)
- **AMD_SPI_ALT_CS_REG** (line 33)
- **AMD_SPI_ALT_SPD_MASK** (line 49)
- **AMD_SPI_ALT_SPD_SHIFT** (line 48)
- **AMD_SPI_BUSY** (line 25)
- **AMD_SPI_CMD_TRIGGER_REG** (line 28)
- **AMD_SPI_CTRL0_REG** (line 22)
- **AMD_SPI_ENA_REG** (line 47)
- **AMD_SPI_EXEC_CMD** (line 23)
- **AMD_SPI_FIFO_BASE** (line 36)
- **AMD_SPI_FIFO_CLEAR** (line 24)
- **AMD_SPI_FIFO_SIZE** (line 42)
- **AMD_SPI_HID2_CMD_START** (line 60)
- **AMD_SPI_HID2_CNTRL** (line 58)
- **AMD_SPI_HID2_DMA_SIZE** (line 45)
- **AMD_SPI_HID2_INPUT_RING_BUF0** (line 56)
- **AMD_SPI_HID2_INT_MASK** (line 61)
- **AMD_SPI_HID2_INT_STATUS** (line 59)
- **AMD_SPI_HID2_OUTPUT_BUF0** (line 57)
- **AMD_SPI_HID2_READ_CNTRL0** (line 64)
- **AMD_SPI_HID2_READ_CNTRL1** (line 65)
- **AMD_SPI_HID2_READ_CNTRL2** (line 66)
- **AMD_SPI_HID2_WRITE_CNTRL0** (line 62)
- **AMD_SPI_HID2_WRITE_CNTRL1** (line 63)
- **AMD_SPI_IO_SLEEP_US** (line 71)
- **AMD_SPI_IO_TIMEOUT_US** (line 72)
- **AMD_SPI_MAX_DATA** (line 44)
- **AMD_SPI_MAX_HZ** (line 68)
- **AMD_SPI_MEM_SIZE** (line 43)
- **AMD_SPI_MIN_HZ** (line 69)
- **AMD_SPI_OPCODE_MASK** (line 31)
- **AMD_SPI_OPCODE_REG** (line 27)
- **AMD_SPI_OP_PP** (line 90)
- **AMD_SPI_OP_PP_RANDOM** (line 91)
- **AMD_SPI_OP_READ** (line 75)
- **AMD_SPI_OP_READ_1_1_2** (line 77)
- **AMD_SPI_OP_READ_1_1_2_4B** (line 84)
- **AMD_SPI_OP_READ_1_1_4** (line 79)
- **AMD_SPI_OP_READ_1_1_4_4B** (line 86)
- **AMD_SPI_OP_READ_1_2_2** (line 78)
- **AMD_SPI_OP_READ_1_2_2_4B** (line 85)
- **AMD_SPI_OP_READ_1_4_4** (line 80)
- **AMD_SPI_OP_READ_1_4_4_4B** (line 87)
- **AMD_SPI_OP_READ_FAST** (line 76)
- **AMD_SPI_OP_READ_FAST_4B** (line 83)
- **AMD_SPI_RX_COUNT_REG** (line 38)
- **AMD_SPI_SPD7_MASK** (line 54)
- **AMD_SPI_SPD7_SHIFT** (line 53)
- **AMD_SPI_SPEED_REG** (line 52)
- **AMD_SPI_SPI100_MASK** (line 51)
- **AMD_SPI_SPI100_SHIFT** (line 50)
- **AMD_SPI_STATUS_REG** (line 39)
- **AMD_SPI_TRIGGER_CMD** (line 29)
- **AMD_SPI_TX_COUNT_REG** (line 37)
