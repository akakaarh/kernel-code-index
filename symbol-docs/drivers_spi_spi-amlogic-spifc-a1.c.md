# drivers/spi/spi-amlogic-spifc-a1.c

Subsystem: drivers/spi

## Functions (18)

### amlogic_spifc_a1_adjust_op_size
- Return type: static int
- Signature: amlogic_spifc_a1_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 294

### amlogic_spifc_a1_drain_buffer
- Return type: static void
- Signature: amlogic_spifc_a1_drain_buffer(struct amlogic_spifc_a1 * spifc,char * buf,u32 len)
- Line: 127

### amlogic_spifc_a1_exec_op
- Return type: static int
- Signature: amlogic_spifc_a1_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 254

### amlogic_spifc_a1_fill_buffer
- Return type: static void
- Signature: amlogic_spifc_a1_fill_buffer(struct amlogic_spifc_a1 * spifc,const char * buf,u32 len)
- Line: 144

### amlogic_spifc_a1_hw_init
- Return type: static void
- Signature: amlogic_spifc_a1_hw_init(struct amlogic_spifc_a1 * spifc)
- Line: 301

### amlogic_spifc_a1_probe
- Return type: static int
- Signature: amlogic_spifc_a1_probe(struct platform_device * pdev)
- Line: 327

### amlogic_spifc_a1_read
- Return type: static int
- Signature: amlogic_spifc_a1_read(struct amlogic_spifc_a1 * spifc,void * buf,u32 size,u32 mode)
- Line: 203

### amlogic_spifc_a1_request
- Return type: static int
- Signature: amlogic_spifc_a1_request(struct amlogic_spifc_a1 * spifc,bool read)
- Line: 113

### amlogic_spifc_a1_resume
- Return type: static int
- Signature: amlogic_spifc_a1_resume(struct device * dev)
- Line: 394

### amlogic_spifc_a1_runtime_resume
- Return type: static int
- Signature: amlogic_spifc_a1_runtime_resume(struct device * dev)
- Line: 425

### amlogic_spifc_a1_runtime_suspend
- Return type: static int
- Signature: amlogic_spifc_a1_runtime_suspend(struct device * dev)
- Line: 416

### amlogic_spifc_a1_set_addr
- Return type: static void
- Signature: amlogic_spifc_a1_set_addr(struct amlogic_spifc_a1 * spifc,u32 addr,u32 addr_cfg)
- Line: 180

### amlogic_spifc_a1_set_cmd
- Return type: static void
- Signature: amlogic_spifc_a1_set_cmd(struct amlogic_spifc_a1 * spifc,u32 cmd_cfg)
- Line: 169

### amlogic_spifc_a1_set_dummy
- Return type: static void
- Signature: amlogic_spifc_a1_set_dummy(struct amlogic_spifc_a1 * spifc,u32 dummy_cfg)
- Line: 193

### amlogic_spifc_a1_set_freq
- Return type: static int
- Signature: amlogic_spifc_a1_set_freq(struct amlogic_spifc_a1 * spifc,u32 freq)
- Line: 239

### amlogic_spifc_a1_suspend
- Return type: static int
- Signature: amlogic_spifc_a1_suspend(struct device * dev)
- Line: 379

### amlogic_spifc_a1_user_init
- Return type: static void
- Signature: amlogic_spifc_a1_user_init(struct amlogic_spifc_a1 * spifc)
- Line: 161

### amlogic_spifc_a1_write
- Return type: static int
- Signature: amlogic_spifc_a1_write(struct amlogic_spifc_a1 * spifc,const void * buf,u32 size,u32 mode)
- Line: 222

## Structs (1)

### amlogic_spifc_a1
- Line: 105
- Members:
  - ctrl: spi_controller *
  - clk: clk *
  - dev: device *
  - base: void __iomem *
  - curr_speed_hz: u32

## Variables (5)

- static **amlogic_spifc_a1_driver** : platform_driver (line 454)
- static **amlogic_spifc_a1_dt_match** : const struct of_device_id[] (line 447)
- static **amlogic_spifc_a1_mem_caps** : const struct spi_controller_mem_caps (line 323)
- static **amlogic_spifc_a1_mem_ops** : const struct spi_controller_mem_ops (line 318)
- static **amlogic_spifc_a1_pm_ops** : const struct dev_pm_ops (line 438)

## Macros (53)

- **SPIFC_A1_ACTIMING0_REG** (line 58)
- **SPIFC_A1_ACTIMING0_VAL** (line 101)
- **SPIFC_A1_AHB_BUS_EN** (line 25)
- **SPIFC_A1_AHB_CTRL_REG** (line 24)
- **SPIFC_A1_AHB_REQ_CTRL_REG** (line 55)
- **SPIFC_A1_AHB_REQ_ENABLE** (line 56)
- **SPIFC_A1_BUFFER_SIZE** (line 75)
- **SPIFC_A1_DBUF_ADDR** (line 69)
- **SPIFC_A1_DBUF_AUTO_UPDATE_ADDR** (line 68)
- **SPIFC_A1_DBUF_CTRL_REG** (line 66)
- **SPIFC_A1_DBUF_DATA_REG** (line 71)
- **SPIFC_A1_DBUF_DIR** (line 67)
- **SPIFC_A1_MAX_HZ** (line 77)
- **SPIFC_A1_MIN_HZ** (line 78)
- **SPIFC_A1_TCLSH** (line 60)
- **SPIFC_A1_TCLSH_VAL** (line 96)
- **SPIFC_A1_TSHSL1** (line 63)
- **SPIFC_A1_TSHSL1_VAL** (line 99)
- **SPIFC_A1_TSHSL2** (line 62)
- **SPIFC_A1_TSHSL2_VAL** (line 98)
- **SPIFC_A1_TSHWL** (line 61)
- **SPIFC_A1_TSHWL_VAL** (line 97)
- **SPIFC_A1_TSLCH** (line 59)
- **SPIFC_A1_TSLCH_VAL** (line 95)
- **SPIFC_A1_TWHSL** (line 64)
- **SPIFC_A1_TWHSL_VAL** (line 100)
- **SPIFC_A1_USER_ADDR**(op) (line 85)
- **SPIFC_A1_USER_ADDR_BYTES** (line 38)
- **SPIFC_A1_USER_ADDR_ENABLE** (line 36)
- **SPIFC_A1_USER_ADDR_MODE** (line 37)
- **SPIFC_A1_USER_ADDR_REG** (line 53)
- **SPIFC_A1_USER_CMD**(op) (line 80)
- **SPIFC_A1_USER_CMD_CODE** (line 35)
- **SPIFC_A1_USER_CMD_ENABLE** (line 33)
- **SPIFC_A1_USER_CMD_MODE** (line 34)
- **SPIFC_A1_USER_CTRL0_REG** (line 27)
- **SPIFC_A1_USER_CTRL1_REG** (line 32)
- **SPIFC_A1_USER_CTRL2_REG** (line 43)
- **SPIFC_A1_USER_CTRL3_REG** (line 48)
- **SPIFC_A1_USER_DATA_UPDATED** (line 30)
- **SPIFC_A1_USER_DBUF_ADDR_REG** (line 73)
- **SPIFC_A1_USER_DIN_BYTES** (line 51)
- **SPIFC_A1_USER_DIN_ENABLE** (line 49)
- **SPIFC_A1_USER_DIN_MODE** (line 50)
- **SPIFC_A1_USER_DOUT_BYTES** (line 41)
- **SPIFC_A1_USER_DOUT_ENABLE** (line 39)
- **SPIFC_A1_USER_DOUT_MODE** (line 40)
- **SPIFC_A1_USER_DUMMY**(op) (line 90)
- **SPIFC_A1_USER_DUMMY_CLK_SYCLES** (line 46)
- **SPIFC_A1_USER_DUMMY_ENABLE** (line 44)
- **SPIFC_A1_USER_DUMMY_MODE** (line 45)
- **SPIFC_A1_USER_REQUEST_ENABLE** (line 28)
- **SPIFC_A1_USER_REQUEST_FINISH** (line 29)
