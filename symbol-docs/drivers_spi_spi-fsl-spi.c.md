# drivers/spi/spi-fsl-spi.c

Subsystem: drivers/spi

## Functions (29)

### fsl_spi_bufs
- Return type: static int
- Signature: fsl_spi_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 252

### fsl_spi_change_mode
- Return type: static void
- Signature: fsl_spi_change_mode(struct spi_device * spi)
- Line: 89

### fsl_spi_cleanup
- Return type: static void
- Signature: fsl_spi_cleanup(struct spi_device * spi)
- Line: 417

### fsl_spi_cpu_bufs
- Return type: static int
- Signature: fsl_spi_cpu_bufs(struct mpc8xxx_spi * mspi,struct spi_transfer * t,unsigned int len)
- Line: 234

### fsl_spi_cpu_irq
- Return type: static void
- Signature: fsl_spi_cpu_irq(struct mpc8xxx_spi * mspi,u32 events)
- Line: 425

### fsl_spi_cs_control
- Return type: static void
- Signature: fsl_spi_cs_control(struct spi_device * spi,bool on)
- Line: 517

### fsl_spi_exit
- Return type: static void __exit
- Signature: fsl_spi_exit(void)
- Line: 803

### fsl_spi_get_type
- Return type: static int
- Signature: fsl_spi_get_type(struct device * dev)
- Line: 77

### fsl_spi_grlib_cs_control
- Return type: static void
- Signature: fsl_spi_grlib_cs_control(struct spi_device * spi,bool on)
- Line: 479

### fsl_spi_grlib_probe
- Return type: static void
- Signature: fsl_spi_grlib_probe(struct device * dev)
- Line: 493

### fsl_spi_grlib_set_shifts
- Return type: static void
- Signature: fsl_spi_grlib_set_shifts(u32 * rx_shift,u32 * tx_shift,int bits_per_word,int msb_first)
- Line: 133

### fsl_spi_init
- Return type: static int __init
- Signature: fsl_spi_init(void)
- Line: 796

### fsl_spi_irq
- Return type: static irqreturn_t
- Signature: fsl_spi_irq(s32 irq,void * context_data)
- Line: 457

### fsl_spi_prepare_message
- Return type: static int
- Signature: fsl_spi_prepare_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 293

### fsl_spi_probe
- Return type: static spi_controller *
- Signature: fsl_spi_probe(struct device * dev,struct resource * mem,unsigned int irq)
- Line: 528

### fsl_spi_qe_cpu_set_shifts
- Return type: static void
- Signature: fsl_spi_qe_cpu_set_shifts(u32 * rx_shift,u32 * tx_shift,int bits_per_word,int msb_first)
- Line: 114

### fsl_spi_setup
- Return type: static int
- Signature: fsl_spi_setup(struct spi_device * spi)
- Line: 368

### fsl_spi_setup_transfer
- Return type: static int
- Signature: fsl_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 177

### fsl_spi_transfer_one
- Return type: static int
- Signature: fsl_spi_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * t)
- Line: 345

### fsl_spi_unprepare_message
- Return type: static int
- Signature: fsl_spi_unprepare_message(struct spi_controller * controller,struct spi_message * msg)
- Line: 362

### legacy_driver_register
- Return type: static void __init
- Signature: legacy_driver_register(void)
- Line: 792

### legacy_driver_register
- Return type: static void __init
- Signature: legacy_driver_register(void)
- Line: 780

### legacy_driver_unregister
- Return type: static void __exit
- Signature: legacy_driver_unregister(void)
- Line: 793

### legacy_driver_unregister
- Return type: static void __exit
- Signature: legacy_driver_unregister(void)
- Line: 785

### mspi_apply_cpu_mode_quirks
- Return type: static void
- Signature: mspi_apply_cpu_mode_quirks(struct spi_mpc8xxx_cs * cs,struct spi_device * spi,struct mpc8xxx_spi * mpc8xxx_spi,int bits_per_word)
- Line: 148

### of_fsl_spi_probe
- Return type: static int
- Signature: of_fsl_spi_probe(struct platform_device * ofdev)
- Line: 634

### of_fsl_spi_remove
- Return type: static void
- Signature: of_fsl_spi_remove(struct platform_device * ofdev)
- Line: 703

### plat_mpc8xxx_spi_probe
- Return type: static int
- Signature: plat_mpc8xxx_spi_probe(struct platform_device * pdev)
- Line: 734

### plat_mpc8xxx_spi_remove
- Return type: static void
- Signature: plat_mpc8xxx_spi_remove(struct platform_device * pdev)
- Line: 755

## Structs (1)

### fsl_spi_match_data
- Line: 52
- Members:
  - type: int

## Variables (6)

- static **legacy_driver_failed** : bool (line 778)
- static **mpc8xxx_spi_driver** : platform_driver (line 770)
- static **of_fsl_spi_driver** : platform_driver (line 717)
- static **of_fsl_spi_fsl_config** : fsl_spi_match_data (line 56)
- static **of_fsl_spi_grlib_config** : fsl_spi_match_data (line 60)
- static **of_fsl_spi_match** : const struct of_device_id[] (line 64)

## Macros (4)

- **IMMR_SPI_CS_OFFSET** (line 42)
- **SPI_BOOT_SEL_BIT** (line 43)
- **TYPE_FSL** (line 49)
- **TYPE_GRLIB** (line 50)
