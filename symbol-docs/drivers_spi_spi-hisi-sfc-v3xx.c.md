# drivers/spi/spi-hisi-sfc-v3xx.c

Subsystem: drivers/spi

## Functions (17)

### hisi_sfc_v3xx_adjust_op_size
- Return type: static int
- Signature: hisi_sfc_v3xx_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 147

### hisi_sfc_v3xx_clear_int
- Return type: static void
- Signature: hisi_sfc_v3xx_clear_int(struct hisi_sfc_v3xx_host * host)
- Line: 94

### hisi_sfc_v3xx_disable_int
- Return type: static void
- Signature: hisi_sfc_v3xx_disable_int(struct hisi_sfc_v3xx_host * host)
- Line: 84

### hisi_sfc_v3xx_dmi_quirk
- Return type: static int __init
- Signature: hisi_sfc_v3xx_dmi_quirk(const struct dmi_system_id * d)
- Line: 399

### hisi_sfc_v3xx_enable_int
- Return type: static void
- Signature: hisi_sfc_v3xx_enable_int(struct hisi_sfc_v3xx_host * host)
- Line: 89

### hisi_sfc_v3xx_exec_op
- Return type: static int
- Signature: hisi_sfc_v3xx_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 359

### hisi_sfc_v3xx_generic_exec_op
- Return type: static int
- Signature: hisi_sfc_v3xx_generic_exec_op(struct hisi_sfc_v3xx_host * host,const struct spi_mem_op * op,u8 chip_select)
- Line: 317

### hisi_sfc_v3xx_handle_completion
- Return type: static int
- Signature: hisi_sfc_v3xx_handle_completion(struct hisi_sfc_v3xx_host * host)
- Line: 104

### hisi_sfc_v3xx_isr
- Return type: static irqreturn_t
- Signature: hisi_sfc_v3xx_isr(int irq,void * data)
- Line: 377

### hisi_sfc_v3xx_probe
- Return type: static int
- Signature: hisi_sfc_v3xx_probe(struct platform_device * pdev)
- Line: 431

### hisi_sfc_v3xx_read_databuf
- Return type: static void
- Signature: hisi_sfc_v3xx_read_databuf(struct hisi_sfc_v3xx_host * host,u8 * to,unsigned int len)
- Line: 198

### hisi_sfc_v3xx_spi_exit
- Return type: static void __exit
- Signature: hisi_sfc_v3xx_spi_exit(void)
- Line: 537

### hisi_sfc_v3xx_spi_init
- Return type: static int __init
- Signature: hisi_sfc_v3xx_spi_init(void)
- Line: 530

### hisi_sfc_v3xx_start_bus
- Return type: static int
- Signature: hisi_sfc_v3xx_start_bus(struct hisi_sfc_v3xx_host * host,const struct spi_mem_op * op,u8 chip_select)
- Line: 273

### hisi_sfc_v3xx_supports_op
- Return type: static bool
- Signature: hisi_sfc_v3xx_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 171

### hisi_sfc_v3xx_wait_cmd_idle
- Return type: static int
- Signature: hisi_sfc_v3xx_wait_cmd_idle(struct hisi_sfc_v3xx_host * host)
- Line: 137

### hisi_sfc_v3xx_write_databuf
- Return type: static void
- Signature: hisi_sfc_v3xx_write_databuf(struct hisi_sfc_v3xx_host * host,const u8 * from,unsigned int len)
- Line: 235

## Structs (1)

### hisi_sfc_v3xx_host
- Line: 75
- Members:
  - dev: device *
  - regbase: void __iomem *
  - max_cmd_dword: int
  - completion: completion *
  - address_mode: u8
  - irq: int

## Variables (6)

- static **hisi_sfc_v3xx_acpi_ids** : const struct acpi_device_id[] (line 516)
- static **hisi_sfc_v3xx_buswidth_override_bits** : int (line 393)
- static **hisi_sfc_v3xx_dmi_quirk_table** : const struct dmi_system_id[] (line 406)
- static **hisi_sfc_v3xx_io_modes** : const int[2][3][3] (line 62)
- static **hisi_sfc_v3xx_mem_ops** : const struct spi_controller_mem_ops (line 371)
- static **hisi_sfc_v3xx_spi_driver** : platform_driver (line 522)

## Macros (31)

- **HISI_SFC_V3XX_CMD_ADDR** (line 37)
- **HISI_SFC_V3XX_CMD_CFG** (line 28)
- **HISI_SFC_V3XX_CMD_CFG_ADDR_EN_MSK** (line 33)
- **HISI_SFC_V3XX_CMD_CFG_CS_SEL_OFF** (line 34)
- **HISI_SFC_V3XX_CMD_CFG_DATA_CNT_OFF** (line 29)
- **HISI_SFC_V3XX_CMD_CFG_DATA_EN_MSK** (line 31)
- **HISI_SFC_V3XX_CMD_CFG_DUMMY_CNT_OFF** (line 32)
- **HISI_SFC_V3XX_CMD_CFG_RW_MSK** (line 30)
- **HISI_SFC_V3XX_CMD_CFG_START_MSK** (line 35)
- **HISI_SFC_V3XX_CMD_DATABUF0** (line 38)
- **HISI_SFC_V3XX_CMD_INS** (line 36)
- **HISI_SFC_V3XX_DIDO** (line 50)
- **HISI_SFC_V3XX_DIO** (line 51)
- **HISI_SFC_V3XX_FULL_DIO** (line 52)
- **HISI_SFC_V3XX_FULL_QIO** (line 55)
- **HISI_SFC_V3XX_GLB_CFG** (line 22)
- **HISI_SFC_V3XX_GLB_CFG_CS0_ADDR_MODE** (line 23)
- **HISI_SFC_V3XX_INT_CLR** (line 27)
- **HISI_SFC_V3XX_INT_MASK** (line 26)
- **HISI_SFC_V3XX_INT_MASK_ALL** (line 41)
- **HISI_SFC_V3XX_INT_MASK_CPLT** (line 42)
- **HISI_SFC_V3XX_INT_MASK_IACCES** (line 44)
- **HISI_SFC_V3XX_INT_MASK_PP_ERR** (line 43)
- **HISI_SFC_V3XX_INT_STAT** (line 25)
- **HISI_SFC_V3XX_QIO** (line 54)
- **HISI_SFC_V3XX_QIQO** (line 53)
- **HISI_SFC_V3XX_RAW_INT_STAT** (line 24)
- **HISI_SFC_V3XX_STD** (line 49)
- **HISI_SFC_V3XX_VERSION** (line 20)
- **HISI_SFC_V3XX_WAIT_POLL_INTERVAL_US** (line 135)
- **HISI_SFC_V3XX_WAIT_TIMEOUT_US** (line 134)
