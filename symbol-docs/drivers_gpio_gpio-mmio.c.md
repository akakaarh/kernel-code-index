# drivers/gpio/gpio-mmio.c

Subsystem: drivers/gpio

## Functions (44)

### gpio_generic_chip_init
- Return type: int
- Signature: gpio_generic_chip_init(struct gpio_generic_chip * chip,const struct gpio_generic_chip_config * cfg)
- Line: 625
- Calls: gpio_mmio_setup_accessors, gpio_mmio_setup_direction, gpio_mmio_setup_io, gpiochip_get_ngpios
- Called by: airoha_gpio_probe, ath79_gpio_probe, blzp1600_gpio_probe, brcmstb_gpio_probe, cdns_gpio_probe, clps711x_gpio_probe, dwapb_gpio_add_port, ep93xx_gpio_probe, ftgpio_gpio_probe, gef_gpio_probe, gpio_mmio_pdev_probe, grgpio_probe, hisi_gpio_probe, hlwd_gpio_probe, idt_gpio_probe, iproc_gpio_probe, ixp4xx_gpio_probe, loongson_gpio_init, ls1x_gpio_probe, mediatek_gpio_bank_probe, men_z127_probe, mlxbf2_gpio_probe, mlxbf3_gpio_probe, mlxbf_gpio_probe, mmio_74xx_gpio_probe, mpc8xxx_probe, mxc_gpio_probe, mxs_gpio_probe, pt_gpio_probe, rda_gpio_probe, realtek_gpio_probe, sdv_gpio_probe, sifive_gpio_probe, spacemit_gpio_add_bank, tb10x_gpio_probe, ts4800_gpio_probe, vf610_gpio_probe, visconti_gpio_probe, xgene_gpio_sb_probe

### gpio_mmio_dir_in
- Return type: static int
- Signature: gpio_mmio_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 388
- Calls: gpio_mmio_dir_return, gpio_mmio_line2mask

### gpio_mmio_dir_in_err
- Return type: static int
- Signature: gpio_mmio_dir_in_err(struct gpio_chip * gc,unsigned int gpio)
- Line: 364

### gpio_mmio_dir_out
- Return type: static void
- Signature: gpio_mmio_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 428
- Calls: gpio_mmio_line2mask
- Called by: gpio_mmio_dir_out_dir_first, gpio_mmio_dir_out_val_first

### gpio_mmio_dir_out_dir_first
- Return type: static int
- Signature: gpio_mmio_dir_out_dir_first(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 442
- Calls: gpio_mmio_dir_out, gpio_mmio_dir_return

### gpio_mmio_dir_out_err
- Return type: static int
- Signature: gpio_mmio_dir_out_err(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 374

### gpio_mmio_dir_out_val_first
- Return type: static int
- Signature: gpio_mmio_dir_out_val_first(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 450
- Calls: gpio_mmio_dir_out, gpio_mmio_dir_return

### gpio_mmio_dir_return
- Return type: static int
- Signature: gpio_mmio_dir_return(struct gpio_chip * gc,unsigned int gpio,bool dir_out)
- Line: 350
- Called by: gpio_mmio_dir_in, gpio_mmio_dir_out_dir_first, gpio_mmio_dir_out_val_first, gpio_mmio_simple_dir_in, gpio_mmio_simple_dir_out

### gpio_mmio_get
- Return type: static int
- Signature: gpio_mmio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 170
- Calls: gpio_mmio_line2mask

### gpio_mmio_get_dir
- Return type: static int
- Signature: gpio_mmio_get_dir(struct gpio_chip * gc,unsigned int gpio)
- Line: 404
- Calls: gpio_mmio_line2mask

### gpio_mmio_get_multiple
- Return type: static int
- Signature: gpio_mmio_get_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 180

### gpio_mmio_get_multiple_be
- Return type: static int
- Signature: gpio_mmio_get_multiple_be(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 194
- Calls: gpio_mmio_line2mask

### gpio_mmio_get_set
- Return type: static int
- Signature: gpio_mmio_get_set(struct gpio_chip * gc,unsigned int gpio)
- Line: 134
- Calls: gpio_mmio_line2mask

### gpio_mmio_get_set_multiple
- Return type: static int
- Signature: gpio_mmio_get_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 150

### gpio_mmio_line2mask
- Return type: static unsigned long
- Signature: gpio_mmio_line2mask(struct gpio_chip * gc,unsigned int line)
- Line: 125
- Called by: gpio_mmio_dir_in, gpio_mmio_dir_out, gpio_mmio_get, gpio_mmio_get_dir, gpio_mmio_get_multiple_be, gpio_mmio_get_set, gpio_mmio_multiple_get_masks, gpio_mmio_set, gpio_mmio_set_set, gpio_mmio_set_with_clear

### gpio_mmio_map
- Return type: static void __iomem *
- Signature: gpio_mmio_map(struct platform_device * pdev,const char * name,resource_size_t sane_sz)
- Line: 703
- Called by: gpio_mmio_pdev_probe

### gpio_mmio_multiple_get_masks
- Return type: static void
- Signature: gpio_mmio_multiple_get_masks(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits,unsigned long * set_mask,unsigned long * clear_mask)
- Line: 275
- Calls: gpio_mmio_line2mask
- Called by: gpio_mmio_set_multiple_single_reg, gpio_mmio_set_multiple_with_clear

### gpio_mmio_pdev_probe
- Return type: static int
- Signature: gpio_mmio_pdev_probe(struct platform_device * pdev)
- Line: 730
- Calls: gpio_generic_chip_init, gpio_mmio_map

### gpio_mmio_read16
- Return type: static unsigned long
- Signature: gpio_mmio_read16(void __iomem * reg)
- Line: 78

### gpio_mmio_read16be
- Return type: static unsigned long
- Signature: gpio_mmio_read16be(void __iomem * reg)
- Line: 110

### gpio_mmio_read32
- Return type: static unsigned long
- Signature: gpio_mmio_read32(void __iomem * reg)
- Line: 88

### gpio_mmio_read32be
- Return type: static unsigned long
- Signature: gpio_mmio_read32be(void __iomem * reg)
- Line: 120

### gpio_mmio_read64
- Return type: static unsigned long
- Signature: gpio_mmio_read64(void __iomem * reg)
- Line: 99

### gpio_mmio_read8
- Return type: static unsigned long
- Signature: gpio_mmio_read8(void __iomem * reg)
- Line: 68

### gpio_mmio_request
- Return type: static int
- Signature: gpio_mmio_request(struct gpio_chip * gc,unsigned int gpio_pin)
- Line: 605
- Calls: gpiochip_generic_request

### gpio_mmio_set
- Return type: static int
- Signature: gpio_mmio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 227
- Calls: gpio_mmio_line2mask

### gpio_mmio_set_multiple
- Return type: static int
- Signature: gpio_mmio_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 313
- Calls: gpio_mmio_set_multiple_single_reg

### gpio_mmio_set_multiple_set
- Return type: static int
- Signature: gpio_mmio_set_multiple_set(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 323
- Calls: gpio_mmio_set_multiple_single_reg

### gpio_mmio_set_multiple_single_reg
- Return type: static void
- Signature: gpio_mmio_set_multiple_single_reg(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits,void __iomem * reg)
- Line: 295
- Calls: gpio_mmio_multiple_get_masks
- Called by: gpio_mmio_set_multiple, gpio_mmio_set_multiple_set

### gpio_mmio_set_multiple_with_clear
- Return type: static int
- Signature: gpio_mmio_set_multiple_with_clear(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 333
- Calls: gpio_mmio_multiple_get_masks

### gpio_mmio_set_none
- Return type: static int
- Signature: gpio_mmio_set_none(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 222

### gpio_mmio_set_set
- Return type: static int
- Signature: gpio_mmio_set_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 258
- Calls: gpio_mmio_line2mask

### gpio_mmio_set_with_clear
- Return type: static int
- Signature: gpio_mmio_set_with_clear(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 244
- Calls: gpio_mmio_line2mask

### gpio_mmio_setup_accessors
- Return type: static int
- Signature: gpio_mmio_setup_accessors(struct device * dev,struct gpio_generic_chip * chip,bool byte_be)
- Line: 458
- Called by: gpio_generic_chip_init

### gpio_mmio_setup_direction
- Return type: static int
- Signature: gpio_mmio_setup_direction(struct gpio_generic_chip * chip,const struct gpio_generic_chip_config * cfg)
- Line: 576
- Called by: gpio_generic_chip_init

### gpio_mmio_setup_io
- Return type: static int
- Signature: gpio_mmio_setup_io(struct gpio_generic_chip * chip,const struct gpio_generic_chip_config * cfg)
- Line: 527
- Called by: gpio_generic_chip_init

### gpio_mmio_simple_dir_in
- Return type: static int
- Signature: gpio_mmio_simple_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 369
- Calls: gpio_mmio_dir_return

### gpio_mmio_simple_dir_out
- Return type: static int
- Signature: gpio_mmio_simple_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 380
- Calls: gpio_mmio_dir_return

### gpio_mmio_write16
- Return type: static void
- Signature: gpio_mmio_write16(void __iomem * reg,unsigned long data)
- Line: 73

### gpio_mmio_write16be
- Return type: static void
- Signature: gpio_mmio_write16be(void __iomem * reg,unsigned long data)
- Line: 105

### gpio_mmio_write32
- Return type: static void
- Signature: gpio_mmio_write32(void __iomem * reg,unsigned long data)
- Line: 83

### gpio_mmio_write32be
- Return type: static void
- Signature: gpio_mmio_write32be(void __iomem * reg,unsigned long data)
- Line: 115

### gpio_mmio_write64
- Return type: static void
- Signature: gpio_mmio_write64(void __iomem * reg,unsigned long data)
- Line: 94

### gpio_mmio_write8
- Return type: static void
- Signature: gpio_mmio_write8(void __iomem * reg,unsigned long data)
- Line: 63

## Variables (3)

- static **gpio_mmio_driver** : platform_driver (line 824)
- static **gpio_mmio_id_table** : const struct platform_device_id[] (line 815)
- static **gpio_mmio_of_match** : const struct of_device_id[] (line 720)
