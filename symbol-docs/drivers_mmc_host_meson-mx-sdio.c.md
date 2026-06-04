# drivers/mmc/host/meson-mx-sdio.c

Subsystem: drivers/mmc

## Functions (17)

### meson_mx_mmc_add_host
- Return type: static int
- Signature: meson_mx_mmc_add_host(struct meson_mx_mmc_host * host)
- Line: 523

### meson_mx_mmc_get_next_cmd
- Return type: static mmc_command *
- Signature: meson_mx_mmc_get_next_cmd(struct mmc_command * cmd)
- Line: 132

### meson_mx_mmc_irq
- Return type: static irqreturn_t
- Signature: meson_mx_mmc_irq(int irq,void * data)
- Line: 403

### meson_mx_mmc_irq_thread
- Return type: static irqreturn_t
- Signature: meson_mx_mmc_irq_thread(int irq,void * irq_data)
- Line: 427

### meson_mx_mmc_map_dma
- Return type: static int
- Signature: meson_mx_mmc_map_dma(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 294

### meson_mx_mmc_probe
- Return type: static int
- Signature: meson_mx_mmc_probe(struct platform_device * pdev)
- Line: 629

### meson_mx_mmc_process_cmd_irq
- Return type: static irqreturn_t
- Signature: meson_mx_mmc_process_cmd_irq(struct meson_mx_mmc_host * host,u32 irqs,u32 send)
- Line: 374

### meson_mx_mmc_read_response
- Return type: static void
- Signature: meson_mx_mmc_read_response(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 347

### meson_mx_mmc_register_clk
- Return type: static clk *
- Signature: meson_mx_mmc_register_clk(struct device * dev,void __iomem * base)
- Line: 571

### meson_mx_mmc_remove
- Return type: static void
- Signature: meson_mx_mmc_remove(struct platform_device * pdev)
- Line: 734

### meson_mx_mmc_request
- Return type: static void
- Signature: meson_mx_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 321

### meson_mx_mmc_request_done
- Return type: static void
- Signature: meson_mx_mmc_request_done(struct meson_mx_mmc_host * host)
- Line: 228

### meson_mx_mmc_set_ios
- Return type: static void
- Signature: meson_mx_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 243

### meson_mx_mmc_slot_pdev
- Return type: static platform_device *
- Signature: meson_mx_mmc_slot_pdev(struct device * parent)
- Line: 494

### meson_mx_mmc_soft_reset
- Return type: static void
- Signature: meson_mx_mmc_soft_reset(struct meson_mx_mmc_host * host)
- Line: 125

### meson_mx_mmc_start_cmd
- Return type: static void
- Signature: meson_mx_mmc_start_cmd(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 143

### meson_mx_mmc_timeout
- Return type: static void
- Signature: meson_mx_mmc_timeout(struct timer_list * t)
- Line: 453

## Structs (2)

### meson_mx_mmc_host
- Line: 107
- Members:
  - cfg_div: clk_divider
  - fixed_div2: clk_fixed_factor
  - controller_dev: device *
  - cfg_div_clk: clk *
  - regmap: regmap *
  - irq: int
  - irq_lock: spinlock_t
  - cmd_timeout: timer_list
  - slot_id: unsigned int
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - error: int

### meson_mx_mmc_host_clkc
- Line: 102
- Members:
  - cfg_div: clk_divider
  - fixed_div2: clk_fixed_factor
  - controller_dev: device *
  - cfg_div_clk: clk *
  - regmap: regmap *
  - irq: int
  - irq_lock: spinlock_t
  - cmd_timeout: timer_list
  - slot_id: unsigned int
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - error: int

## Variables (3)

- static **meson_mx_mmc_driver** : platform_driver (line 755)
- static **meson_mx_mmc_of_match** : const struct of_device_id[] (line 748)
- static **meson_mx_mmc_ops** : mmc_host_ops (line 487)

## Macros (62)

- **MESON_MX_SDIO_ADDR** (line 93)
- **MESON_MX_SDIO_ARGU** (line 31)
- **MESON_MX_SDIO_BOUNCE_REQ_SIZE** (line 98)
- **MESON_MX_SDIO_CONF** (line 44)
- **MESON_MX_SDIO_CONF_BUS_WIDTH** (line 52)
- **MESON_MX_SDIO_CONF_CMD_ARGUMENT_BITS_MASK** (line 49)
- **MESON_MX_SDIO_CONF_CMD_CLK_DIV_SHIFT** (line 45)
- **MESON_MX_SDIO_CONF_CMD_CLK_DIV_WIDTH** (line 46)
- **MESON_MX_SDIO_CONF_CMD_DISABLE_CRC** (line 47)
- **MESON_MX_SDIO_CONF_CMD_OUT_AT_POSITIVE_EDGE** (line 48)
- **MESON_MX_SDIO_CONF_DATA_LATCH_AT_NEGATIVE_EDGE** (line 51)
- **MESON_MX_SDIO_CONF_M_ENDIAN_MASK** (line 53)
- **MESON_MX_SDIO_CONF_RESP_LATCH_AT_NEGATIVE_EDGE** (line 50)
- **MESON_MX_SDIO_CONF_WRITE_CRC_OK_STATUS_MASK** (line 55)
- **MESON_MX_SDIO_CONF_WRITE_NWR_MASK** (line 54)
- **MESON_MX_SDIO_EXT** (line 95)
- **MESON_MX_SDIO_EXT_DATA_RW_NUMBER_MASK** (line 96)
- **MESON_MX_SDIO_IRQC** (line 71)
- **MESON_MX_SDIO_IRQC_ARC_CMD_INT_EN** (line 73)
- **MESON_MX_SDIO_IRQC_ARC_IF_INT_EN** (line 72)
- **MESON_MX_SDIO_IRQC_FORCE_DATA_CLK** (line 75)
- **MESON_MX_SDIO_IRQC_FORCE_DATA_CMD** (line 76)
- **MESON_MX_SDIO_IRQC_FORCE_DATA_DAT_MASK** (line 77)
- **MESON_MX_SDIO_IRQC_FORCE_HALT** (line 79)
- **MESON_MX_SDIO_IRQC_HALT_HOLE** (line 80)
- **MESON_MX_SDIO_IRQC_IF_CONFIG_MASK** (line 74)
- **MESON_MX_SDIO_IRQC_SOFT_RESET** (line 78)
- **MESON_MX_SDIO_IRQS** (line 57)
- **MESON_MX_SDIO_IRQS_AMRISC_TIMING_OUT_INT_EN** (line 67)
- **MESON_MX_SDIO_IRQS_ARC_TIMING_OUT_INT_EN** (line 68)
- **MESON_MX_SDIO_IRQS_CMD_BUSY** (line 59)
- **MESON_MX_SDIO_IRQS_CMD_INT** (line 64)
- **MESON_MX_SDIO_IRQS_DATA_READ_CRC16_OK** (line 61)
- **MESON_MX_SDIO_IRQS_DATA_WRITE_CRC16_OK** (line 62)
- **MESON_MX_SDIO_IRQS_IF_INT** (line 63)
- **MESON_MX_SDIO_IRQS_RESP_CRC7_OK** (line 60)
- **MESON_MX_SDIO_IRQS_STATUS_INFO_MASK** (line 65)
- **MESON_MX_SDIO_IRQS_STATUS_STATE_MACHINE_MASK** (line 58)
- **MESON_MX_SDIO_IRQS_TIMING_OUT_COUNT_MASK** (line 69)
- **MESON_MX_SDIO_IRQS_TIMING_OUT_INT** (line 66)
- **MESON_MX_SDIO_MAX_SLOTS** (line 100)
- **MESON_MX_SDIO_MULT** (line 82)
- **MESON_MX_SDIO_MULT_DAT0_DAT1_SWAPPED** (line 89)
- **MESON_MX_SDIO_MULT_DAT1_DAT0_SWAPPED** (line 90)
- **MESON_MX_SDIO_MULT_MEMORY_STICK_ENABLE** (line 84)
- **MESON_MX_SDIO_MULT_MEMORY_STICK_SCLK_ALWAYS** (line 85)
- **MESON_MX_SDIO_MULT_PORT_SEL_MASK** (line 83)
- **MESON_MX_SDIO_MULT_RESP_READ_INDEX_MASK** (line 91)
- **MESON_MX_SDIO_MULT_STREAM_8BITS_MODE** (line 87)
- **MESON_MX_SDIO_MULT_STREAM_ENABLE** (line 86)
- **MESON_MX_SDIO_MULT_WR_RD_OUT_INDEX** (line 88)
- **MESON_MX_SDIO_RESPONSE_CRC16_BITS** (line 99)
- **MESON_MX_SDIO_SEND** (line 33)
- **MESON_MX_SDIO_SEND_CHECK_DAT0_BUSY** (line 39)
- **MESON_MX_SDIO_SEND_CMD_RESP_BITS_MASK** (line 35)
- **MESON_MX_SDIO_SEND_COMMAND_INDEX_MASK** (line 34)
- **MESON_MX_SDIO_SEND_DATA** (line 40)
- **MESON_MX_SDIO_SEND_REPEAT_PACKAGE_TIMES_MASK** (line 42)
- **MESON_MX_SDIO_SEND_RESP_CRC7_FROM_8** (line 38)
- **MESON_MX_SDIO_SEND_RESP_HAS_DATA** (line 37)
- **MESON_MX_SDIO_SEND_RESP_WITHOUT_CRC7** (line 36)
- **MESON_MX_SDIO_SEND_USE_INT_WINDOW** (line 41)
