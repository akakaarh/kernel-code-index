# drivers/gpio/gpiolib.c

Subsystem: drivers/gpio

## Functions (200)

### desc_free_label
- Return type: static void
- Signature: desc_free_label(struct rcu_head * rh)
- Line: 138

### desc_set_label
- Return type: static int
- Signature: desc_set_label(struct gpio_desc * desc,const char * label)
- Line: 143
- Called by: gpiod_free_commit, gpiod_request_commit, gpiod_set_consumer_name

### desc_to_gpio
- Return type: int
- Signature: desc_to_gpio(const struct gpio_desc * desc)
- Line: 230
- Called by: gpio_set_open_drain_value_commit, gpio_set_open_source_value_commit, gpiochip_fwd_desc_add, gpiod_direction_input_nonotify, gpiod_direction_output_raw_commit, gpiod_export, gpiod_get_array_value_complex, gpiod_get_raw_value_commit, gpiod_set_array_value_complex, gpiod_set_raw_value_commit, hte_edge_setup, nmk_gpio_dbg_show_one

### function_name_or_default
- Return type: static const char *
- Signature: function_name_or_default(const char * con_id)
- Line: 2696
- Called by: gpiochip_request_own_desc, gpiod_configure_flags, gpiod_find_and_request, gpiod_find_by_fwnode

### fwnode_gpiod_get_index
- Return type: gpio_desc *
- Signature: fwnode_gpiod_get_index(struct fwnode_handle * fwnode,const char * con_id,int index,enum gpiod_flags flags,const char * label)
- Line: 4871
- Calls: gpiod_find_and_request

### gpio_bus_match
- Return type: static int
- Signature: gpio_bus_match(struct device * dev,const struct device_driver * drv)
- Line: 61

### gpio_chip_get_multiple
- Return type: static int
- Signature: gpio_chip_get_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 3428
- Calls: gpiochip_get
- Called by: gpiod_get_array_value_complex

### gpio_chip_get_value
- Return type: static int
- Signature: gpio_chip_get_value(struct gpio_chip * gc,const struct gpio_desc * desc)
- Line: 3380
- Calls: gpiochip_get, gpiod_hwgpio
- Called by: gpiod_get_raw_value_commit, gpiolib_dbg_show

### gpio_chip_match_by_fwnode
- Return type: static int
- Signature: gpio_chip_match_by_fwnode(struct gpio_chip * gc,const void * fwnode)
- Line: 1484

### gpio_chip_match_by_label
- Return type: static int
- Signature: gpio_chip_match_by_label(struct gpio_chip * gc,const void * label)
- Line: 1464

### gpio_desc_table_match
- Return type: static gpio_desc *
- Signature: gpio_desc_table_match(struct device * dev,const char * con_id,unsigned int idx,unsigned long * flags,struct gpiod_lookup_table * table)
- Line: 4601
- Calls: gpio_device_find_by_label, gpio_device_get_chip, gpio_device_get_desc, gpio_name_to_desc
- Called by: gpiod_find

### gpio_device_chip_cmp
- Return type: static bool
- Signature: gpio_device_chip_cmp(struct gpio_device * gdev,struct gpio_chip * gc)
- Line: 3457
- Called by: gpiod_get_array_value_complex, gpiod_set_array_value_complex

### gpio_device_find
- Return type: gpio_device *
- Signature: gpio_device_find(const void * data,int (* match)(struct gpio_chip * gc,const void * data))
- Line: 1436
- Calls: gpio_device_get
- Called by: acpi_get_gpiod, gpio_device_find_by_fwnode, gpio_device_find_by_label, gpiolib_sysfs_init, of_find_gpio_device_by_node, of_find_gpio_device_by_xlate

### gpio_device_find_by_fwnode
- Return type: gpio_device *
- Signature: gpio_device_find_by_fwnode(const struct fwnode_handle * fwnode)
- Line: 1507
- Calls: gpio_device_find
- Called by: gpiod_shared_desc_create, swnode_get_gpio_device

### gpio_device_find_by_label
- Return type: gpio_device *
- Signature: gpio_device_find_by_label(const char * label)
- Line: 1478
- Calls: gpio_device_find
- Called by: gpio_desc_table_match, swnode_get_gpio_device

### gpio_device_get
- Return type: gpio_device *
- Signature: gpio_device_get(struct gpio_device * gdev)
- Line: 1520
- Called by: gpio_chrdev_open, gpio_device_find, gpiod_request, lineevent_create, linehandle_create, lineinfo_changed_notify, linereq_create

### gpio_device_get_base
- Return type: int
- Signature: gpio_device_get_base(struct gpio_device * gdev)
- Line: 299

### gpio_device_get_chip
- Return type: gpio_chip *
- Signature: gpio_device_get_chip(struct gpio_device * gdev)
- Line: 335
- Called by: gpio_desc_table_match, gpiod_to_chip, of_get_named_gpiod_flags, of_gpio_notify

### gpio_device_get_desc
- Return type: gpio_desc *
- Signature: gpio_device_get_desc(struct gpio_device * gdev,unsigned int hwnum)
- Line: 211
- Called by: acpi_get_gpiod, do_chip_export_store, gpio_desc_table_match, gpiochip_get_desc, lineevent_create, linehandle_create, lineinfo_get, lineinfo_get_v1, linereq_create, nmk_gpio_dbg_show_one, swnode_find_gpio

### gpio_device_get_label
- Return type: const char *
- Signature: gpio_device_get_label(struct gpio_device * gdev)
- Line: 313
- Called by: devm_gpiod_shared_get, gpio_shared_make_adev, gpiochip_setup_shared

### gpio_device_put
- Return type: void
- Signature: gpio_device_put(struct gpio_device * gdev)
- Line: 1531
- Called by: gpio_chrdev_open, gpio_chrdev_release, gpio_shared_release, gpiochip_add_data_with_key, gpiochip_remove, gpiochip_setup_devs, gpiod_free, lineevent_free, linehandle_free, lineinfo_changed_func, linereq_free

### gpio_device_to_device
- Return type: device *
- Signature: gpio_device_to_device(struct gpio_device * gdev)
- Line: 1548

### gpio_do_set_config
- Return type: int
- Signature: gpio_do_set_config(struct gpio_desc * desc,unsigned long config)
- Line: 2778
- Calls: gpiod_hwgpio
- Called by: debounce_setup, gpio_set_config_with_argument, gpiod_set_config

### gpio_name_to_desc
- Return type: static gpio_desc *
- Signature: gpio_name_to_desc(const char * const name)
- Line: 551
- Called by: gpio_desc_table_match, gpiochip_set_desc_names

### gpio_set_bias
- Return type: static int
- Signature: gpio_set_bias(struct gpio_desc * desc)
- Line: 2843
- Calls: gpio_set_config_with_argument_optional
- Called by: gpiod_direction_input_nonotify, gpiod_direction_output_nonotify

### gpio_set_config
- Return type: static int
- Signature: gpio_set_config(struct gpio_desc * desc,enum pin_config_param mode)
- Line: 2838
- Calls: gpio_set_config_with_argument
- Called by: gpiod_direction_output_nonotify

### gpio_set_config_with_argument
- Return type: static int
- Signature: gpio_set_config_with_argument(struct gpio_desc * desc,enum pin_config_param mode,u32 argument)
- Line: 2805
- Calls: gpio_do_set_config
- Called by: gpio_set_config, gpio_set_config_with_argument_optional

### gpio_set_config_with_argument_optional
- Return type: static int
- Signature: gpio_set_config_with_argument_optional(struct gpio_desc * desc,enum pin_config_param mode,u32 argument)
- Line: 2815
- Calls: gpio_set_config_with_argument, gpiod_hwgpio
- Called by: gpio_set_bias, gpio_set_debounce_timeout, gpiod_set_transitory

### gpio_set_debounce_timeout
- Return type: int
- Signature: gpio_set_debounce_timeout(struct gpio_desc * desc,unsigned int debounce)
- Line: 2885
- Calls: gpio_set_config_with_argument_optional, gpiod_line_state_notify
- Called by: acpi_dev_gpio_irq_wake_get_by, acpi_gpio_set_debounce_timeout

### gpio_set_open_drain_value_commit
- Return type: static int
- Signature: gpio_set_open_drain_value_commit(struct gpio_desc * desc,bool value)
- Line: 3699
- Calls: desc_to_gpio, gpiochip_direction_input, gpiochip_direction_output, gpiod_hwgpio
- Called by: gpiod_set_array_value_complex, gpiod_set_value_nocheck

### gpio_set_open_source_value_commit
- Return type: static int
- Signature: gpio_set_open_source_value_commit(struct gpio_desc * desc,bool value)
- Line: 3728
- Calls: desc_to_gpio, gpiochip_direction_input, gpiochip_direction_output, gpiod_hwgpio
- Called by: gpiod_set_array_value_complex, gpiod_set_value_nocheck

### gpio_to_desc
- Return type: gpio_desc *
- Signature: gpio_to_desc(unsigned gpio)
- Line: 170
- Called by: acpi_populate_gpio_lookup, export_store, gpio_free, gpio_request, unexport_store

### gpiochip_add_data_with_key
- Return type: int
- Signature: gpiochip_add_data_with_key(struct gpio_chip * gc,void * data,struct lock_class_key * lock_key,struct lock_class_key * request_key)
- Line: 1137
- Calls: acpi_gpiochip_add, acpi_gpiochip_remove, gpio_device_put, gpio_device_teardown_shared, gpiochip_add_irqchip, gpiochip_add_pin_ranges, gpiochip_choose_fwnode, gpiochip_find_base_unlocked, gpiochip_free_hogs, gpiochip_free_valid_mask, gpiochip_get_ngpios, gpiochip_hog_lines, gpiochip_init_valid_mask, gpiochip_irqchip_free_valid_mask, gpiochip_irqchip_init_hw, gpiochip_irqchip_init_valid_mask, gpiochip_irqchip_remove, gpiochip_line_is_valid, gpiochip_remove_pin_ranges, gpiochip_set_data, gpiochip_set_desc_names, gpiochip_set_names, gpiochip_setup_dev, gpiochip_setup_shared, gpiodev_add_to_list_unlocked, of_gpiochip_add, of_gpiochip_remove
- Called by: devm_gpiochip_add_data_with_key

### gpiochip_add_hog
- Return type: int
- Signature: gpiochip_add_hog(struct gpio_chip * gc,struct fwnode_handle * fwnode)
- Line: 936
- Calls: gpiochip_get_desc, gpiod_hog, of_gpiochip_get_lflags
- Called by: gpiochip_hog_lines, of_gpio_notify

### gpiochip_add_irqchip
- Return type: static int
- Signature: gpiochip_add_irqchip(struct gpio_chip * gc,struct lock_class_key * lock_key,struct lock_class_key * request_key)
- Line: 2330
- Calls: acpi_gpiochip_request_interrupts, gpiochip_hierarchy_create_domain, gpiochip_hierarchy_is_hierarchical, gpiochip_irqchip_add_allocated_domain, gpiochip_set_irq_hooks, gpiochip_simple_create_domain
- Called by: gpiochip_add_data_with_key

### gpiochip_add_irqchip
- Return type: static int
- Signature: gpiochip_add_irqchip(struct gpio_chip * gc,struct lock_class_key * lock_key,struct lock_class_key * request_key)
- Line: 2183
- Calls: acpi_gpiochip_request_interrupts, gpiochip_hierarchy_create_domain, gpiochip_hierarchy_is_hierarchical, gpiochip_irqchip_add_allocated_domain, gpiochip_set_irq_hooks, gpiochip_simple_create_domain
- Called by: gpiochip_add_data_with_key

### gpiochip_add_pin_range_with_pins
- Return type: int
- Signature: gpiochip_add_pin_range_with_pins(struct gpio_chip * gc,const char * pinctl_name,unsigned int gpio_offset,unsigned int pin_offset,unsigned int const * pins,unsigned int npins)
- Line: 2483

### gpiochip_add_pin_ranges
- Return type: static int
- Signature: gpiochip_add_pin_ranges(struct gpio_chip * gc)
- Line: 782
- Called by: gpiochip_add_data_with_key

### gpiochip_add_pingroup_range
- Return type: int
- Signature: gpiochip_add_pingroup_range(struct gpio_chip * gc,struct pinctrl_dev * pctldev,unsigned int gpio_offset,const char * pin_group)
- Line: 2425
- Called by: of_gpiochip_add_pin_range, tegra186_gpio_add_pin_ranges

### gpiochip_allocate_mask
- Return type: static unsigned long *
- Signature: gpiochip_allocate_mask(struct gpio_chip * gc)
- Line: 685
- Called by: gpiochip_init_valid_mask, gpiochip_irqchip_init_valid_mask

### gpiochip_apply_reserved_ranges
- Return type: static int
- Signature: gpiochip_apply_reserved_ranges(struct gpio_chip * gc)
- Line: 718
- Calls: gpiochip_count_reserved_ranges
- Called by: gpiochip_init_valid_mask

### gpiochip_child_offset_to_irq_noop
- Return type: static unsigned int
- Signature: gpiochip_child_offset_to_irq_noop(struct gpio_chip * gc,unsigned int offset)
- Line: 1766

### gpiochip_choose_fwnode
- Return type: static fwnode_handle *
- Signature: gpiochip_choose_fwnode(struct gpio_chip * gc)
- Line: 1091
- Called by: gpiochip_add_data_with_key, gpiochip_get_ngpios

### gpiochip_count_reserved_ranges
- Return type: static unsigned int
- Signature: gpiochip_count_reserved_ranges(struct gpio_chip * gc)
- Line: 705
- Called by: gpiochip_apply_reserved_ranges, gpiochip_init_valid_mask

### gpiochip_direction_input
- Return type: static int
- Signature: gpiochip_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 2898
- Called by: gpio_set_open_drain_value_commit, gpio_set_open_source_value_commit, gpiod_direction_input_nonotify

### gpiochip_direction_output
- Return type: static int
- Signature: gpiochip_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 2914
- Called by: gpio_set_open_drain_value_commit, gpio_set_open_source_value_commit, gpiod_direction_output_raw_commit

### gpiochip_disable_irq
- Return type: void
- Signature: gpiochip_disable_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4238
- Calls: gpiochip_get_desc
- Called by: adnp_irq_mask, adp5585_irq_mask, altera_gpio_irq_mask, aspeed_gpio_irq_set_mask, aspeed_sgpio_irq_set_mask, ath79_gpio_irq_mask, bcm_kona_gpio_irq_mask, blzp1600_gpio_irq_disable, cdns_gpio_irq_mask, crystalcove_irq_mask, dln2_irq_mask, dwapb_irq_mask, ep93xx_gpio_irq_mask, ep93xx_gpio_irq_mask_ack, ftgpio_gpio_mask_irq, gnr_gpio_irq_mask, gpio_irq_mask, gpio_mpsse_irq_disable, gpio_rcar_irq_disable, gpio_siox_irq_mask, gpiochip_irq_disable, gpiochip_irq_mask, grgpio_irq_mask, hisi_gpio_irq_set_mask, hlwd_gpio_irq_mask, idt_gpio_mask, iproc_gpio_irq_mask, ixp4xx_gpio_mask_irq, kempld_irq_mask, ljca_irq_mask, lpc18xx_gpio_pin_ic_mask, max732x_irq_mask, max77620_gpio_irq_mask, max77759_gpio_irq_mask, mediatek_gpio_irq_mask, mlxbf2_gpio_irq_disable, mlxbf3_gpio_irq_disable, mpc8xxx_irq_mask, mpfs_gpio_irq_mask, msc313_gpio_irq_mask, nct6694_irq_mask, nmk_gpio_irq_mask, nvl_gpio_irq_mask, omap_gpio_mask_irq, pca953x_irq_mask, pcf857x_irq_disable, pl061_irq_mask, rda_gpio_irq_mask, realtek_gpio_irq_mask, rtd_gpio_disable_irq, sch_irq_mask, sifive_gpio_irq_disable, sprd_eic_irq_mask, sprd_gpio_irq_mask, sprd_pmic_eic_irq_mask, stmpe_gpio_irq_mask, tc3589x_gpio_irq_mask, tegra186_irq_mask, tegra_gpio_irq_mask, thunderx_gpio_irq_disable, timbgpio_irq_disable, tng_irq_mask, tqmx86_gpio_irq_mask, vf610_gpio_irq_mask, visconti_gpio_mask_irq, wcove_irq_mask, xgene_gpio_sb_irq_mask, xgpio_irq_mask, xlp_gpio_irq_disable, zynq_gpio_irq_mask

### gpiochip_dup_line_label
- Return type: char *
- Signature: gpiochip_dup_line_label(struct gpio_chip * gc,unsigned int offset)
- Line: 2674
- Calls: gpiochip_get_desc, gpiod_get_label
- Called by: nmk_gpio_dbg_show_one, stmpe_dbg_show_one, wm831x_gpio_dbg_show, wm8994_gpio_dbg_show

### gpiochip_enable_irq
- Return type: void
- Signature: gpiochip_enable_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4248
- Calls: gpiochip_get_desc
- Called by: adnp_irq_unmask, adp5585_irq_unmask, altera_gpio_irq_unmask, aspeed_gpio_irq_set_mask, aspeed_sgpio_irq_set_mask, ath79_gpio_irq_unmask, bcm_kona_gpio_irq_unmask, blzp1600_gpio_irq_enable, cdns_gpio_irq_unmask, crystalcove_irq_unmask, dln2_irq_unmask, dwapb_irq_unmask, ep93xx_gpio_irq_unmask, ftgpio_gpio_unmask_irq, gnr_gpio_irq_unmask, gpio_irq_unmask, gpio_mpsse_irq_enable, gpio_rcar_irq_enable, gpio_siox_irq_unmask, gpiochip_irq_enable, gpiochip_irq_unmask, grgpio_irq_unmask, hisi_gpio_irq_clr_mask, hlwd_gpio_irq_unmask, idt_gpio_unmask, iproc_gpio_irq_unmask, ixp4xx_gpio_irq_unmask, kempld_irq_unmask, ljca_irq_unmask, lpc18xx_gpio_pin_ic_unmask, max732x_irq_unmask, max77620_gpio_irq_unmask, max77759_gpio_irq_unmask, mediatek_gpio_irq_unmask, mlxbf2_gpio_irq_enable, mlxbf3_gpio_irq_enable, mpc8xxx_irq_unmask, mpfs_gpio_irq_unmask, msc313_gpio_irq_unmask, nct6694_irq_unmask, nmk_gpio_irq_unmask, nvl_gpio_irq_unmask, omap_gpio_unmask_irq, pca953x_irq_unmask, pcf857x_irq_enable, pl061_irq_unmask, rda_gpio_irq_unmask, realtek_gpio_irq_unmask, rtd_gpio_enable_irq, sch_irq_unmask, sifive_gpio_irq_enable, sprd_eic_irq_unmask, sprd_gpio_irq_unmask, sprd_pmic_eic_irq_unmask, stmpe_gpio_irq_unmask, tc3589x_gpio_irq_unmask, tegra186_irq_unmask, tegra_gpio_irq_unmask, thunderx_gpio_irq_enable, timbgpio_irq_enable, tng_irq_unmask, tqmx86_gpio_irq_unmask, vf610_gpio_irq_unmask, visconti_gpio_unmask_irq, wcove_irq_unmask, xgene_gpio_sb_irq_unmask, xgpio_irq_unmask, xlp_gpio_irq_enable, zynq_gpio_irq_unmask

### gpiochip_find_base_unlocked
- Return type: static int
- Signature: gpiochip_find_base_unlocked(u16 ngpio)
- Line: 350
- Called by: gpiochip_add_data_with_key

### gpiochip_free_hogs
- Return type: static void
- Signature: gpiochip_free_hogs(struct gpio_chip * gc)
- Line: 5135
- Calls: gpiochip_free_own_desc
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpiochip_free_mask
- Return type: static void
- Signature: gpiochip_free_mask(unsigned long ** p)
- Line: 699
- Called by: gpiochip_free_valid_mask, gpiochip_irqchip_free_valid_mask

### gpiochip_free_own_desc
- Return type: void
- Signature: gpiochip_free_own_desc(struct gpio_desc * desc)
- Line: 2761
- Calls: gpiod_free_commit
- Called by: acpi_gpio_adr_space_handler, acpi_gpiochip_alloc_event, acpi_gpiochip_free_interrupts, acpi_gpiochip_free_regions, gpio_twl4030_power_off_action, gpiochip_free_hogs, mvebu_pwm_free, of_gpiochip_remove_hog

### gpiochip_free_remaining_irqs
- Return type: static void
- Signature: gpiochip_free_remaining_irqs(struct gpio_chip * gc)
- Line: 861
- Calls: gpiod_free_irqs
- Called by: gpiochip_remove

### gpiochip_free_valid_mask
- Return type: static void
- Signature: gpiochip_free_valid_mask(struct gpio_chip * gc)
- Line: 777
- Calls: gpiochip_free_mask
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpiochip_generic_config
- Return type: int
- Signature: gpiochip_generic_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 2396
- Called by: dwapb_gpio_set_config, mxc_gpio_generic_config, omap_gpio_set_config, rockchip_gpio_set_config, rtd_gpio_set_config, tng_gpio_set_config

### gpiochip_generic_free
- Return type: void
- Signature: gpiochip_generic_free(struct gpio_chip * gc,unsigned int offset)
- Line: 2376
- Called by: mxc_gpio_free

### gpiochip_generic_request
- Return type: int
- Signature: gpiochip_generic_request(struct gpio_chip * gc,unsigned int offset)
- Line: 2360
- Called by: gpio_mmio_request, mxc_gpio_request

### gpiochip_get
- Return type: static int
- Signature: gpiochip_get(struct gpio_chip * gc,unsigned int offset)
- Line: 3362
- Called by: gpio_chip_get_multiple, gpio_chip_get_value

### gpiochip_get_data
- Return type: void *
- Signature: gpiochip_get_data(struct gpio_chip * gc)
- Line: 1081
- Called by: __aspeed_gpio_set, __cgbc_gpio_set, __davinci_direction, __mpc52xx_simple_gpio_set, __mpc52xx_wkup_gpio_set, __xgene_gpio_set, adnp_gpio_dbg_show, adnp_gpio_direction_input, adnp_gpio_direction_output, adnp_gpio_get, adnp_gpio_set, adnp_irq_bus_lock, adnp_irq_bus_unlock, adnp_irq_mask, adnp_irq_set_type, adnp_irq_unmask, adp5520_gpio_direction_input, adp5520_gpio_direction_output, adp5520_gpio_get_value, adp5520_gpio_set_value, adp5585_gpio_direction_input, adp5585_gpio_direction_output, adp5585_gpio_get_direction, adp5585_gpio_get_value, adp5585_gpio_request, adp5585_gpio_set_config, adp5585_gpio_set_value, adp5585_irq_bus_lock, adp5585_irq_bus_sync_unlock, adp5585_irq_mask, adp5585_irq_set_type, adp5585_irq_unmask, airoha_dir_set, airoha_get_dir, altera_gpio_direction_input, altera_gpio_direction_output, altera_gpio_get, altera_gpio_irq_edge_handler, altera_gpio_irq_leveL_high_handler, altera_gpio_irq_mask, altera_gpio_irq_set_type, altera_gpio_irq_unmask, altera_gpio_set, altr_a10sr_gpio_get, altr_a10sr_gpio_set, amd_fch_gpio_direction_input, amd_fch_gpio_direction_output, amd_fch_gpio_get, amd_fch_gpio_get_direction, amd_fch_gpio_set, amd_gpio_dirin, amd_gpio_dirout, amd_gpio_free, amd_gpio_get, amd_gpio_request, amd_gpio_set, arizona_gpio_direction_in, arizona_gpio_direction_out, arizona_gpio_get, arizona_gpio_set, aspeed_gpio_copro_grab_gpio, aspeed_gpio_copro_release_gpio, aspeed_gpio_dir_in, aspeed_gpio_dir_out, aspeed_gpio_get, aspeed_gpio_get_direction, aspeed_gpio_irq_handler, aspeed_gpio_request, aspeed_gpio_reset_tolerance, aspeed_gpio_set, aspeed_init_irq_valid_mask, aspeed_sgpio_dir_out, aspeed_sgpio_get, aspeed_sgpio_irq_handler, aspeed_sgpio_reset_tolerance, aspeed_sgpio_set, bcm_kona_gpio_direction_input, bcm_kona_gpio_direction_output, bcm_kona_gpio_free, bcm_kona_gpio_get, bcm_kona_gpio_get_dir, bcm_kona_gpio_request, bcm_kona_gpio_set, bcm_kona_gpio_set_debounce, bcm_kona_gpio_to_irq, bd71815_gpio_set_config, bd71815gpo_get, bd71815gpo_set, bd71828_gpio_get, bd71828_gpio_set, bd71828_gpio_set_config, bd72720_gpio_set_config, bd72720_valid_mask, bd72720gpio_get, bd72720gpo_direction_get, bd72720gpo_set, bd9571mwv_gpio_direction_input, bd9571mwv_gpio_direction_output, bd9571mwv_gpio_get, bd9571mwv_gpio_get_direction, bd9571mwv_gpio_set, blzp1600_gpio_set_debounce, brcmstb_gpio_gc_to_priv, brcmstb_gpio_irq_ack, brcmstb_gpio_irq_mask, brcmstb_gpio_irq_mask_ack, brcmstb_gpio_irq_set_type, brcmstb_gpio_irq_set_wake, brcmstb_gpio_irq_unmask, brcmstb_gpio_of_xlate, bt8xxgpio_gpio_direction_input, bt8xxgpio_gpio_direction_output, bt8xxgpio_gpio_get, bt8xxgpio_gpio_set, cdns_gpio_free, cdns_gpio_irq_handler, cdns_gpio_irq_mask, cdns_gpio_irq_set_type, cdns_gpio_irq_unmask, cdns_gpio_request, cgbc_gpio_direction_input, cgbc_gpio_direction_output, cgbc_gpio_direction_set, cgbc_gpio_get, cgbc_gpio_get_direction, cgbc_gpio_set, chip_direction_input, chip_direction_output, chip_gpio_request, chip_to_pxachip, creg_gpio_set, cros_ec_gpio_get, cros_ec_gpio_get_direction, cros_ec_gpio_set, crystalcove_bus_lock, crystalcove_bus_sync_unlock, crystalcove_gpio_dbg_show, crystalcove_gpio_dir_in, crystalcove_gpio_dir_out, crystalcove_gpio_get, crystalcove_gpio_set, crystalcove_irq_mask, crystalcove_irq_type, crystalcove_irq_unmask, da9052_gpio_direction_input, da9052_gpio_direction_output, da9052_gpio_get, da9052_gpio_set, da9052_gpio_to_irq, da9055_gpio_direction_input, da9055_gpio_direction_output, da9055_gpio_get, da9055_gpio_set, da9055_gpio_to_irq, davinci_get_direction, davinci_gpio_get, davinci_gpio_set, disable_debounce, dln2_gpio_direction_output, dln2_gpio_free, dln2_gpio_get, dln2_gpio_get_direction, dln2_gpio_request, dln2_gpio_set, dln2_gpio_set_config, dln2_gpio_set_direction, dln2_irq_bus_lock, dln2_irq_bus_unlock, dln2_irq_mask, dln2_irq_set_type, dln2_irq_unmask, dwapb_gpio_set_debounce, egpio_direction_input, egpio_direction_output, egpio_get, egpio_get_direction, egpio_set, enable_debounce, exar_direction_input, exar_direction_output, exar_get_direction, exar_get_value, exar_set_value, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, ftgpio_gpio_ack_irq, ftgpio_gpio_irq_handler, ftgpio_gpio_mask_irq, ftgpio_gpio_set_config, ftgpio_gpio_set_irq_type, ftgpio_gpio_unmask_irq, gen_74x164_get_value, gen_74x164_set_multiple, gen_74x164_set_value, get_blzp1600_gpio_from_irq_data, get_blzp1600_gpio_from_irq_desc, gnr_gpio_configure_line, gnr_gpio_get, gnr_gpio_get_direction, gnr_gpio_irq_ack, gnr_gpio_irq_mask_unmask, gnr_gpio_irq_set_type, gnr_gpio_request, gpio_bank_base, gpio_fwd_delay, gpio_fwd_direction_input, gpio_fwd_direction_output, gpio_fwd_get, gpio_fwd_get_direction, gpio_fwd_get_multiple_locked, gpio_fwd_request, gpio_fwd_set, gpio_fwd_set_config, gpio_fwd_set_multiple_locked, gpio_fwd_to_irq, gpio_latch_set, gpio_latch_set_can_sleep, gpio_lmux_gpio_get, gpio_mockup_dirin, gpio_mockup_dirout, gpio_mockup_free, gpio_mockup_get, gpio_mockup_get_direction, gpio_mockup_get_multiple, gpio_mockup_request, gpio_mockup_set, gpio_mockup_set_config, gpio_mockup_set_multiple, gpio_mockup_to_irq, gpio_mpsse_direction_input, gpio_mpsse_direction_output, gpio_mpsse_get_direction, gpio_mpsse_get_multiple, gpio_mpsse_set_multiple, gpio_rcar_config_general_input_output_mode, gpio_rcar_free, gpio_rcar_get, gpio_rcar_get_direction, gpio_rcar_get_multiple, gpio_rcar_irq_disable, gpio_rcar_irq_enable, gpio_rcar_irq_set_type, gpio_rcar_irq_set_wake, gpio_rcar_request, gpio_rcar_set, gpio_rcar_set_multiple, gpio_reg, gpio_reg_and_bit, gpio_regmap_get, gpio_regmap_get_direction, gpio_regmap_set, gpio_regmap_set_direction, gpio_regmap_set_with_clear, gpio_shared_proxy_direction_input, gpio_shared_proxy_direction_output, gpio_shared_proxy_free, gpio_shared_proxy_get, gpio_shared_proxy_get_cansleep, gpio_shared_proxy_get_direction, gpio_shared_proxy_request, gpio_shared_proxy_set, gpio_shared_proxy_set_cansleep, gpio_shared_proxy_set_config, gpio_shared_proxy_to_irq, gpio_sim_dbg_show, gpio_sim_direction_input, gpio_sim_direction_output, gpio_sim_free, gpio_sim_get, gpio_sim_get_direction, gpio_sim_get_multiple, gpio_sim_request, gpio_sim_set, gpio_sim_set_config, gpio_sim_set_multiple, gpio_sim_to_irq, gpio_siox_get, gpio_siox_irq_ack, gpio_siox_irq_mask, gpio_siox_irq_set_type, gpio_siox_irq_unmask, gpio_siox_set, gpio_to_irq_banked, gpio_to_irq_unbanked, gpio_to_priv, gpiochip_fwd_delay_of_xlate, grgpio_to_irq, gw_pld_get8, gw_pld_input8, gw_pld_output8, hlwd_gpio_irq_ack, hlwd_gpio_irq_mask, hlwd_gpio_irq_print_chip, hlwd_gpio_irq_set_type, hlwd_gpio_irq_unmask, hlwd_gpio_irqhandler, idt_gpio_ack, idt_gpio_dispatch, idt_gpio_irq_init_hw, idt_gpio_irq_set_type, idt_gpio_mask, idt_gpio_unmask, imx_scu_gpio_get, imx_scu_gpio_set, ioh_gpio_direction_input, ioh_gpio_direction_output, ioh_gpio_get, ioh_gpio_set, ioh_gpio_to_irq, it87_gpio_direction_in, it87_gpio_direction_out, it87_gpio_get, it87_gpio_request, it87_gpio_set, ixp4xx_gpio_irq_ack, ixp4xx_gpio_irq_set_type, ixp4xx_gpio_irq_unmask, kempld_gpio_direction_input, kempld_gpio_direction_output, kempld_gpio_get, kempld_gpio_get_direction, kempld_gpio_get_multiple, kempld_gpio_set, kempld_gpio_set_multiple, kempld_irq_bus_lock, kempld_irq_bus_sync_unlock, kempld_irq_mask, kempld_irq_set_type, kempld_irq_unmask, keystone_gpio_set, ljca_gpio_direction_input, ljca_gpio_direction_output, ljca_gpio_get_direction, ljca_gpio_get_value, ljca_gpio_init_valid_mask, ljca_gpio_set_config, ljca_gpio_set_value, ljca_irq_bus_lock, ljca_irq_bus_unlock, ljca_irq_mask, ljca_irq_set_type, ljca_irq_unmask, logicvc_gpio_get, logicvc_gpio_set, lp3943_gpio_direction_input, lp3943_gpio_direction_output, lp3943_gpio_free, lp3943_gpio_get, lp3943_gpio_request, lp3943_gpio_set, lp873x_gpio_direction_output, lp873x_gpio_get, lp873x_gpio_request, lp873x_gpio_set, lp873x_gpio_set_config, lp87565_gpio_direction_input, lp87565_gpio_direction_output, lp87565_gpio_get, lp87565_gpio_get_direction, lp87565_gpio_request, lp87565_gpio_set, lp87565_gpio_set_config, lpc18xx_gpio_direction, lpc18xx_gpio_get, lpc18xx_gpio_set, lpc32xx_gpi_get_value, lpc32xx_gpio_dir_input_p012, lpc32xx_gpio_dir_input_p3, lpc32xx_gpio_dir_out_always, lpc32xx_gpio_dir_output_p012, lpc32xx_gpio_dir_output_p3, lpc32xx_gpio_get_value_p012, lpc32xx_gpio_get_value_p3, lpc32xx_gpio_set_value_p012, lpc32xx_gpio_set_value_p3, lpc32xx_gpo_get_value, lpc32xx_gpo_set_value, ls1x_gpio_free, ls1x_gpio_request, ltq_mm_set, macsmc_gpio_get, macsmc_gpio_get_direction, macsmc_gpio_init_valid_mask, macsmc_gpio_set, madera_gpio_direction_in, madera_gpio_direction_out, madera_gpio_get, madera_gpio_get_direction, madera_gpio_set, max3191x_get, max3191x_get_multiple, max3191x_set_config, max7301_get, max7301_set, max732x_gpio_direction_input, max732x_gpio_direction_output, max732x_gpio_get_value, max732x_gpio_set_mask, max732x_irq_bus_lock, max732x_irq_bus_sync_unlock, max732x_irq_mask, max732x_irq_set_type, max732x_irq_unmask, max77620_gpio_bus_lock, max77620_gpio_bus_sync_unlock, max77620_gpio_dir_input, max77620_gpio_dir_output, max77620_gpio_get, max77620_gpio_get_dir, max77620_gpio_irq_init_hw, max77620_gpio_irq_mask, max77620_gpio_irq_unmask, max77620_gpio_set, max77620_gpio_set_config, max77620_gpio_set_irq_type, max77650_gpio_direction_input, max77650_gpio_direction_output, max77650_gpio_get_direction, max77650_gpio_get_value, max77650_gpio_set_config, max77650_gpio_set_value, max77650_gpio_to_irq, max77759_gpio_bus_lock, max77759_gpio_bus_sync_unlock, max77759_gpio_direction_helper, max77759_gpio_get_direction, max77759_gpio_get_value, max77759_gpio_irq_mask, max77759_gpio_irq_unmask, max77759_gpio_set_irq_type, max77759_gpio_set_value, mb86s70_gpio_direction_input, mb86s70_gpio_direction_output, mb86s70_gpio_free, mb86s70_gpio_get, mb86s70_gpio_request, mb86s70_gpio_set, mc33880_set, men_z127_debounce, men_z127_set_single_ended, mlxbf2_gpio_direction_input, mlxbf2_gpio_direction_output, mlxbf2_gpio_irq_disable, mlxbf2_gpio_irq_enable, mlxbf2_gpio_irq_print_chip, mlxbf2_gpio_irq_set_type, mlxbf3_gpio_irq_disable, mlxbf3_gpio_irq_enable, mlxbf3_gpio_irq_set_type, mmio_74xx_dir_in, mmio_74xx_dir_out, mmio_74xx_get_direction, moxtet_gpio_direction_input, moxtet_gpio_direction_output, moxtet_gpio_get_direction, moxtet_gpio_get_value, moxtet_gpio_set_value, mpc5121_gpio_dir_out, mpc5125_gpio_dir_out, mpc52xx_simple_gpio_dir_in, mpc52xx_simple_gpio_dir_out, mpc52xx_simple_gpio_get, mpc52xx_wkup_gpio_dir_in, mpc52xx_wkup_gpio_dir_out, mpc52xx_wkup_gpio_get, mpc8572_gpio_get, mpc8xxx_gpio_to_irq, mpfs_gpio_direction_input, mpfs_gpio_direction_output, mpfs_gpio_get, mpfs_gpio_get_direction, mpfs_gpio_irq_mask, mpfs_gpio_irq_set_type, mpfs_gpio_irq_unmask, mpfs_gpio_set, mpsse_ensure_supported, mpsse_init_valid_mask, mpsse_irq_init_valid_mask, msc313_gpio_direction_input, msc313_gpio_direction_output, msc313_gpio_get, msc313_gpio_set, msc313e_gpio_child_to_parent_hwirq, mtk_gpio_r32, mtk_gpio_w32, mvebu_gpio_blink, mvebu_gpio_dbg_show, mvebu_gpio_direction_input, mvebu_gpio_direction_output, mvebu_gpio_get, mvebu_gpio_get_direction, mvebu_gpio_set, mvebu_gpio_to_irq, mxc_gpio_to_irq, mxs_gpio_get_direction, mxs_gpio_to_irq, nct6694_direction_input, nct6694_direction_output, nct6694_get_direction, nct6694_get_value, nct6694_init_valid_mask, nct6694_irq_bus_lock, nct6694_irq_bus_sync_unlock, nct6694_irq_set_type, nct6694_set_config, nct6694_set_value, nmk_gpio_dbg_show_one, nmk_gpio_get_dir, nmk_gpio_get_input, nmk_gpio_irq_ack, nmk_gpio_irq_mask, nmk_gpio_irq_print_chip, nmk_gpio_irq_set_type, nmk_gpio_irq_set_wake, nmk_gpio_irq_shutdown, nmk_gpio_irq_startup, nmk_gpio_irq_unmask, nmk_gpio_make_input, nmk_gpio_make_output, nmk_gpio_set_output, npcm_sgpio_dir_in, npcm_sgpio_get, npcm_sgpio_get_direction, npcm_sgpio_irq_handler, npcm_sgpio_irq_init_valid_mask, npcm_sgpio_set, nvl_gpio_get, nvl_gpio_irq_ack, nvl_gpio_irq_mask_unmask, octeon_gpio_dir_in, octeon_gpio_dir_out, octeon_gpio_get, octeon_gpio_set, omap_gpio_debounce, omap_gpio_free, omap_gpio_get, omap_gpio_get_direction, omap_gpio_get_multiple, omap_gpio_input, omap_gpio_output, omap_gpio_request, omap_gpio_set, omap_gpio_set_multiple, omap_irq_data_get_bank, palmas_gpio_get, palmas_gpio_input, palmas_gpio_output, palmas_gpio_set, palmas_gpio_to_irq, pca953x_gpio_direction_input, pca953x_gpio_direction_output, pca953x_gpio_get_direction, pca953x_gpio_get_multiple, pca953x_gpio_get_value, pca953x_gpio_set_config, pca953x_gpio_set_multiple, pca953x_gpio_set_value, pca953x_irq_bus_lock, pca953x_irq_bus_sync_unlock, pca953x_irq_mask, pca953x_irq_set_type, pca953x_irq_set_wake, pca953x_irq_shutdown, pca953x_irq_unmask, pca9570_get, pca9570_set, pcf857x_get, pcf857x_get_multiple, pcf857x_input, pcf857x_output, pcf857x_set_multiple, pch_gpio_direction_input, pch_gpio_direction_output, pch_gpio_get, pch_gpio_set, pch_gpio_to_irq, pisosr_gpio_get, pisosr_gpio_get_multiple, pl061_direction_input, pl061_direction_output, pl061_get_direction, pl061_get_value, pl061_irq_ack, pl061_irq_handler, pl061_irq_mask, pl061_irq_set_wake, pl061_irq_type, pl061_irq_unmask, pl061_set_value, pt_gpio_free, pt_gpio_request, rc5t583_gpio_dir_input, rc5t583_gpio_dir_output, rc5t583_gpio_free, rc5t583_gpio_get, rc5t583_gpio_set, rc5t583_gpio_to_irq, rda_gpio_irq_handler, rda_gpio_irq_mask, rda_gpio_set_irq, rda_gpio_update, rdc_gpio_config, rdc_gpio_get_value, rdc_gpio_set_value, rdc_gpio_set_value_impl, realtek_gpio_irq_handler, realtek_gpio_irq_init, rockchip_gpio_get, rockchip_gpio_get_direction, rockchip_gpio_set, rockchip_gpio_set_debounce, rockchip_gpio_set_direction, rockchip_gpio_to_irq, rpi_exp_gpio_dir_in, rpi_exp_gpio_dir_out, rpi_exp_gpio_get, rpi_exp_gpio_get_direction, rpi_exp_gpio_get_polarity, rpi_exp_gpio_set, rtd_gpio_disable_irq, rtd_gpio_enable_irq, rtd_gpio_get, rtd_gpio_get_direction, rtd_gpio_irq_set_type, rtd_gpio_set, rtd_gpio_set_debounce, rtd_gpio_set_direction, sch311x_gpio_direction_in, sch311x_gpio_direction_out, sch311x_gpio_free, sch311x_gpio_get, sch311x_gpio_get_direction, sch311x_gpio_request, sch311x_gpio_set, sch311x_gpio_set_config, sch_gpio_direction_in, sch_gpio_direction_out, sch_gpio_get, sch_gpio_get_direction, sch_gpio_set, sch_irq_ack, sch_irq_mask_unmask, sch_irq_type, set_debounce, sgpio_set_value, sifive_gpio_child_to_parent_hwirq, sifive_gpio_irq_disable, sifive_gpio_irq_enable, sifive_gpio_irq_eoi, sifive_gpio_irq_set_type, spacemit_of_node_instance_match, spics_free, spics_request, spics_set_value, sprd_eic_get, sprd_eic_handle_one_type, sprd_eic_irq_ack, sprd_eic_irq_mask, sprd_eic_irq_set_type, sprd_eic_irq_unmask, sprd_eic_read, sprd_eic_set_debounce, sprd_eic_toggle_trigger, sprd_eic_update, sprd_gpio_irq_handler, sprd_gpio_read, sprd_gpio_update, sprd_pmic_eic_bus_lock, sprd_pmic_eic_bus_sync_unlock, sprd_pmic_eic_irq_mask, sprd_pmic_eic_irq_set_type, sprd_pmic_eic_irq_unmask, sprd_pmic_eic_read, sprd_pmic_eic_set_debounce, sprd_pmic_eic_update, stmpe_dbg_show_one, stmpe_gpio_direction_input, stmpe_gpio_direction_output, stmpe_gpio_get, stmpe_gpio_get_direction, stmpe_gpio_irq_lock, stmpe_gpio_irq_mask, stmpe_gpio_irq_set_type, stmpe_gpio_irq_sync_unlock, stmpe_gpio_irq_unmask, stmpe_gpio_request, stmpe_gpio_set, stmpe_init_irq_valid_mask, syscon_gpio_dir_in, syscon_gpio_dir_out, syscon_gpio_get, syscon_gpio_set, tb10x_gpio_to_irq, tc3589x_gpio_direction_input, tc3589x_gpio_direction_output, tc3589x_gpio_get, tc3589x_gpio_get_direction, tc3589x_gpio_irq_lock, tc3589x_gpio_irq_mask, tc3589x_gpio_irq_set_type, tc3589x_gpio_irq_sync_unlock, tc3589x_gpio_irq_unmask, tc3589x_gpio_set, tc3589x_gpio_set_config, tegra186_gpio_add_pin_ranges, tegra186_gpio_child_offset_to_irq, tegra186_gpio_direction_input, tegra186_gpio_direction_output, tegra186_gpio_dis_hw_ts, tegra186_gpio_en_hw_ts, tegra186_gpio_get, tegra186_gpio_get_direction, tegra186_gpio_irq_domain_translate, tegra186_gpio_of_xlate, tegra186_gpio_populate_parent_fwspec, tegra186_gpio_set, tegra186_gpio_set_config, tegra186_init_valid_mask, tegra_gpio_direction_input, tegra_gpio_direction_output, tegra_gpio_free, tegra_gpio_get, tegra_gpio_get_direction, tegra_gpio_irq_ack, tegra_gpio_irq_mask, tegra_gpio_irq_release_resources, tegra_gpio_irq_request_resources, tegra_gpio_irq_set_type, tegra_gpio_irq_set_wake, tegra_gpio_irq_shutdown, tegra_gpio_irq_unmask, tegra_gpio_set, tegra_gpio_set_debounce, thunderx_gpio_child_to_parent_hwirq, thunderx_gpio_dir_in, thunderx_gpio_dir_out, thunderx_gpio_get, thunderx_gpio_get_direction, thunderx_gpio_irq_ack, thunderx_gpio_irq_mask, thunderx_gpio_irq_mask_ack, thunderx_gpio_irq_set_type, thunderx_gpio_irq_unmask, thunderx_gpio_request, thunderx_gpio_set, thunderx_gpio_set_config, thunderx_gpio_set_multiple, timbgpio_gpio_get, timbgpio_to_irq, timbgpio_update_bit, tng_gpio_add_pin_ranges, tng_gpio_direction_input, tng_gpio_direction_output, tng_gpio_set, tng_gpio_set_debounce, tng_irq_ack, tng_irq_handler, tng_irq_init_hw, tng_irq_mask, tng_irq_set_type, tng_irq_set_wake, tng_irq_unmask, tpic2810_set_mask_bits, tps65086_gpio_direction_output, tps65086_gpio_get, tps65086_gpio_set, tps65214_gpio_change_direction, tps65214_gpio_get_direction, tps65218_gpio_get, tps65218_gpio_request, tps65218_gpio_set, tps65218_gpio_set_config, tps65219_gpio_change_direction, tps65219_gpio_direction_input, tps65219_gpio_direction_output, tps65219_gpio_get, tps65219_gpio_get_direction, tps65219_gpio_set, tps6586x_gpio_get, tps6586x_gpio_output, tps6586x_gpio_set, tps6586x_gpio_to_irq, tps65910_gpio_get, tps65910_gpio_input, tps65910_gpio_output, tps65910_gpio_set, tps65912_gpio_direction_input, tps65912_gpio_direction_output, tps65912_gpio_get, tps65912_gpio_get_direction, tps65912_gpio_set, tps68470_gpio_get, tps68470_gpio_get_direction, tps68470_gpio_input, tps68470_gpio_output, tps68470_gpio_set, tqmx86_gpio_direction_input, tqmx86_gpio_direction_output, tqmx86_gpio_get, tqmx86_gpio_get_direction, tqmx86_gpio_irq_handler, tqmx86_gpio_irq_mask, tqmx86_gpio_irq_set_type, tqmx86_gpio_irq_unmask, tqmx86_gpio_set, ts4900_gpio_direction_input, ts4900_gpio_direction_output, ts4900_gpio_get, ts4900_gpio_get_direction, ts4900_gpio_set, ts5500_gpio_get, ts5500_gpio_input, ts5500_gpio_output, ts5500_gpio_set, ts5500_gpio_to_irq, twl6040gpo_get, twl6040gpo_set, twl_direction_in, twl_direction_out, twl_free, twl_get, twl_get_direction, twl_request, twl_set, twl_to_irq, uniphier_gpio_bank_write, uniphier_gpio_offset_read, usbio_gpio_get, usbio_gpio_get_bank_and_pin, usbio_gpio_set, usbio_gpio_update_config, vf610_gpio_irq_ack, vf610_gpio_irq_handler, vf610_gpio_irq_mask, vf610_gpio_irq_set_type, vf610_gpio_irq_set_wake, vf610_gpio_irq_unmask, virtio_gpio_direction_input, virtio_gpio_direction_output, virtio_gpio_free, virtio_gpio_get, virtio_gpio_get_direction, virtio_gpio_irq_bus_lock, virtio_gpio_irq_bus_sync_unlock, virtio_gpio_irq_disable, virtio_gpio_irq_enable, virtio_gpio_irq_mask, virtio_gpio_irq_set_type, virtio_gpio_irq_unmask, virtio_gpio_set, visconti_gpio_irq_print_chip, visconti_gpio_irq_set_type, vprbrd_gpioa_direction_input, vprbrd_gpioa_direction_output, vprbrd_gpioa_get, vprbrd_gpioa_set, vprbrd_gpiob_direction_input, vprbrd_gpiob_direction_output, vprbrd_gpiob_get, vprbrd_gpiob_set, vx855gpio_direction_input, vx855gpio_get, vx855gpio_set, wcd_gpio_direction_input, wcd_gpio_direction_output, wcd_gpio_get, wcd_gpio_get_direction, wcd_gpio_set, wcove_bus_lock, wcove_bus_sync_unlock, wcove_gpio_dbg_show, wcove_gpio_dir_in, wcove_gpio_dir_out, wcove_gpio_get, wcove_gpio_get_direction, wcove_gpio_set, wcove_gpio_set_config, wcove_irq_mask, wcove_irq_type, wcove_irq_unmask, winbond_gpio_direction_in, winbond_gpio_direction_out, winbond_gpio_get, winbond_gpio_set, wm831x_gpio_dbg_show, wm831x_gpio_direction_in, wm831x_gpio_direction_out, wm831x_gpio_get, wm831x_gpio_set, wm831x_gpio_to_irq, wm831x_set_config, wm8350_gpio_direction_in, wm8350_gpio_direction_out, wm8350_gpio_get, wm8350_gpio_set, wm8350_gpio_to_irq, wm8994_gpio_dbg_show, wm8994_gpio_direction_in, wm8994_gpio_direction_out, wm8994_gpio_get, wm8994_gpio_request, wm8994_gpio_set, wm8994_gpio_set_config, wm8994_gpio_to_irq, xgene_gpio_dir_in, xgene_gpio_dir_out, xgene_gpio_get, xgene_gpio_get_direction, xgene_gpio_sb_to_irq, xgene_gpio_set, xgpio_dir_in, xgpio_dir_out, xgpio_get, xgpio_set, xgpio_set_multiple, xlp_gpio_dir_input, xlp_gpio_dir_output, xlp_gpio_get, xlp_gpio_irq_disable, xlp_gpio_irq_mask_ack, xlp_gpio_irq_unmask, xlp_gpio_set, xlp_gpio_set_irq_type, xra1403_dbg_show, xra1403_direction_input, xra1403_direction_output, xra1403_get, xra1403_get_direction, xra1403_set, xway_stp_get, xway_stp_request, xway_stp_set, zevio_gpio_direction_input, zevio_gpio_direction_output, zevio_gpio_get, zevio_gpio_set, zynq_gpio_dir_in, zynq_gpio_dir_out, zynq_gpio_get_direction, zynq_gpio_get_value, zynq_gpio_irq_ack, zynq_gpio_irq_mask, zynq_gpio_irq_unmask, zynq_gpio_irqhandler, zynq_gpio_set_irq_type, zynq_gpio_set_value, zynq_gpio_set_wake

### gpiochip_get_desc
- Return type: gpio_desc *
- Signature: gpiochip_get_desc(struct gpio_chip * gc,unsigned int hwnum)
- Line: 188
- Calls: gpio_device_get_desc
- Called by: gpiochip_add_hog, gpiochip_disable_irq, gpiochip_dup_line_label, gpiochip_enable_irq, gpiochip_lock_as_irq, gpiochip_request_own_desc, gpiochip_unlock_as_irq, of_xlate_and_get_gpiod_flags

### gpiochip_get_direction
- Return type: static int
- Signature: gpiochip_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 423
- Called by: gpiod_direction_input_nonotify, gpiod_direction_output_raw_commit, gpiod_get_direction

### gpiochip_get_ngpios
- Return type: int
- Signature: gpiochip_get_ngpios(struct gpio_chip * gc,struct device * dev)
- Line: 1102
- Calls: gpiochip_choose_fwnode
- Called by: gpio_generic_chip_init, gpio_regmap_register, gpiochip_add_data_with_key

### gpiochip_hierarchy_create_domain
- Return type: static irq_domain *
- Signature: gpiochip_hierarchy_create_domain(struct gpio_chip * gc)
- Line: 1831
- Calls: gpiochip_hierarchy_setup_domain_ops, gpiochip_set_hierarchical_irqchip
- Called by: gpiochip_add_irqchip

### gpiochip_hierarchy_create_domain
- Return type: static irq_domain *
- Signature: gpiochip_hierarchy_create_domain(struct gpio_chip * gc)
- Line: 1907
- Calls: gpiochip_hierarchy_setup_domain_ops, gpiochip_set_hierarchical_irqchip
- Called by: gpiochip_add_irqchip

### gpiochip_hierarchy_irq_domain_alloc
- Return type: static int
- Signature: gpiochip_hierarchy_irq_domain_alloc(struct irq_domain * d,unsigned int irq,unsigned int nr_irqs,void * data)
- Line: 1694

### gpiochip_hierarchy_irq_domain_translate
- Return type: static int
- Signature: gpiochip_hierarchy_irq_domain_translate(struct irq_domain * d,struct irq_fwspec * fwspec,unsigned long * hwirq,unsigned int * type)
- Line: 1672

### gpiochip_hierarchy_is_hierarchical
- Return type: static bool
- Signature: gpiochip_hierarchy_is_hierarchical(struct gpio_chip * gc)
- Line: 1866
- Called by: gpiochip_add_irqchip

### gpiochip_hierarchy_is_hierarchical
- Return type: static bool
- Signature: gpiochip_hierarchy_is_hierarchical(struct gpio_chip * gc)
- Line: 1912
- Called by: gpiochip_add_irqchip

### gpiochip_hierarchy_setup_domain_ops
- Return type: static void
- Signature: gpiochip_hierarchy_setup_domain_ops(struct irq_domain_ops * ops)
- Line: 1812
- Called by: gpiochip_hierarchy_create_domain

### gpiochip_hog_lines
- Return type: static int
- Signature: gpiochip_hog_lines(struct gpio_chip * gc)
- Line: 1026
- Calls: gpiochip_add_hog
- Called by: gpiochip_add_data_with_key

### gpiochip_init_valid_mask
- Return type: static int
- Signature: gpiochip_init_valid_mask(struct gpio_chip * gc)
- Line: 754
- Calls: gpiochip_allocate_mask, gpiochip_apply_reserved_ranges, gpiochip_count_reserved_ranges
- Called by: gpiochip_add_data_with_key

### gpiochip_irq_disable
- Return type: static void
- Signature: gpiochip_irq_disable(struct irq_data * d)
- Line: 2094
- Calls: gpiochip_disable_irq

### gpiochip_irq_domain_activate
- Return type: static int
- Signature: gpiochip_irq_domain_activate(struct irq_domain * domain,struct irq_data * data,bool reserve)
- Line: 1785
- Calls: gpiochip_lock_as_irq

### gpiochip_irq_domain_deactivate
- Return type: static void
- Signature: gpiochip_irq_domain_deactivate(struct irq_domain * domain,struct irq_data * data)
- Line: 1803
- Calls: gpiochip_unlock_as_irq

### gpiochip_irq_enable
- Return type: static void
- Signature: gpiochip_irq_enable(struct irq_data * d)
- Line: 2085
- Calls: gpiochip_enable_irq

### gpiochip_irq_map
- Return type: static int
- Signature: gpiochip_irq_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hwirq)
- Line: 1932
- Calls: gpiochip_irqchip_irq_valid

### gpiochip_irq_mask
- Return type: static void
- Signature: gpiochip_irq_mask(struct irq_data * d)
- Line: 2065
- Calls: gpiochip_disable_irq

### gpiochip_irq_relres
- Return type: void
- Signature: gpiochip_irq_relres(struct irq_data * d)
- Line: 2056
- Calls: gpiochip_relres_irq

### gpiochip_irq_reqres
- Return type: int
- Signature: gpiochip_irq_reqres(struct irq_data * d)
- Line: 2047
- Calls: gpiochip_reqres_irq

### gpiochip_irq_select
- Return type: static int
- Signature: gpiochip_irq_select(struct irq_domain * d,struct irq_fwspec * fwspec,enum irq_domain_bus_token bus_token)
- Line: 1981
- Calls: of_gpiochip_instance_match

### gpiochip_irq_unmap
- Return type: static void
- Signature: gpiochip_irq_unmap(struct irq_domain * d,unsigned int irq)
- Line: 1971

### gpiochip_irq_unmask
- Return type: static void
- Signature: gpiochip_irq_unmask(struct irq_data * d)
- Line: 2075
- Calls: gpiochip_enable_irq

### gpiochip_irqchip_add_allocated_domain
- Return type: static int
- Signature: gpiochip_irqchip_add_allocated_domain(struct gpio_chip * gc,struct irq_domain * domain,bool allocated_externally)
- Line: 2148
- Called by: gpiochip_add_irqchip, gpiochip_irqchip_add_domain

### gpiochip_irqchip_add_domain
- Return type: int
- Signature: gpiochip_irqchip_add_domain(struct gpio_chip * gc,struct irq_domain * domain)
- Line: 2321
- Calls: gpiochip_irqchip_add_allocated_domain
- Called by: gpio_regmap_register

### gpiochip_irqchip_free_valid_mask
- Return type: static void
- Signature: gpiochip_irqchip_free_valid_mask(struct gpio_chip * gc)
- Line: 2347
- Calls: gpiochip_free_mask
- Called by: gpiochip_add_data_with_key, gpiochip_irqchip_remove

### gpiochip_irqchip_free_valid_mask
- Return type: static void
- Signature: gpiochip_irqchip_free_valid_mask(struct gpio_chip * gc)
- Line: 1586
- Calls: gpiochip_free_mask
- Called by: gpiochip_add_data_with_key, gpiochip_irqchip_remove

### gpiochip_irqchip_init_hw
- Return type: static int
- Signature: gpiochip_irqchip_init_hw(struct gpio_chip * gc)
- Line: 2338
- Called by: gpiochip_add_data_with_key

### gpiochip_irqchip_init_hw
- Return type: static int
- Signature: gpiochip_irqchip_init_hw(struct gpio_chip * gc)
- Line: 1560
- Called by: gpiochip_add_data_with_key

### gpiochip_irqchip_init_valid_mask
- Return type: static int
- Signature: gpiochip_irqchip_init_valid_mask(struct gpio_chip * gc)
- Line: 2343
- Calls: gpiochip_allocate_mask
- Called by: gpiochip_add_data_with_key

### gpiochip_irqchip_init_valid_mask
- Return type: static int
- Signature: gpiochip_irqchip_init_valid_mask(struct gpio_chip * gc)
- Line: 1570
- Calls: gpiochip_allocate_mask
- Called by: gpiochip_add_data_with_key

### gpiochip_irqchip_irq_valid
- Return type: static bool
- Signature: gpiochip_irqchip_irq_valid(const struct gpio_chip * gc,unsigned int offset)
- Line: 1591
- Calls: gpiochip_line_is_valid
- Called by: gpiochip_irq_map, gpiochip_irqchip_remove, gpiochip_to_irq

### gpiochip_irqchip_remove
- Return type: static void
- Signature: gpiochip_irqchip_remove(struct gpio_chip * gc)
- Line: 2336
- Calls: acpi_gpiochip_free_interrupts, gpiochip_irqchip_free_valid_mask, gpiochip_irqchip_irq_valid
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpiochip_irqchip_remove
- Return type: static void
- Signature: gpiochip_irqchip_remove(struct gpio_chip * gc)
- Line: 2263
- Calls: acpi_gpiochip_free_interrupts, gpiochip_irqchip_free_valid_mask, gpiochip_irqchip_irq_valid
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpiochip_line_is_irq
- Return type: bool
- Signature: gpiochip_line_is_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4265

### gpiochip_line_is_open_drain
- Return type: bool
- Signature: gpiochip_line_is_open_drain(struct gpio_chip * gc,unsigned int offset)
- Line: 4298
- Called by: tps65218_gpio_request

### gpiochip_line_is_open_source
- Return type: bool
- Signature: gpiochip_line_is_open_source(struct gpio_chip * gc,unsigned int offset)
- Line: 4307
- Called by: tps65218_gpio_request

### gpiochip_line_is_persistent
- Return type: bool
- Signature: gpiochip_line_is_persistent(struct gpio_chip * gc,unsigned int offset)
- Line: 4316
- Called by: arizona_gpio_direction_in, arizona_gpio_direction_out

### gpiochip_line_is_valid
- Return type: bool
- Signature: gpiochip_line_is_valid(const struct gpio_chip * gc,unsigned int offset)
- Line: 814
- Called by: export_gpio_desc, gpio_desc_to_lineinfo, gpio_rcar_resume, gpiochip_add_data_with_key, gpiochip_irqchip_irq_valid, gpiod_request_commit

### gpiochip_lock_as_irq
- Return type: int
- Signature: gpiochip_lock_as_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4179
- Calls: gpiochip_get_desc, gpiod_get_direction
- Called by: acpi_gpiochip_alloc_event, em_gio_irq_reqres, gpio_sim_irq_requested, gpio_sysfs_request_irq, gpiochip_irq_domain_activate, gpiochip_reqres_irq, tegra_gpio_irq_set_type, uniphier_gpio_irq_domain_activate, xgene_gpio_sb_domain_activate

### gpiochip_populate_parent_fwspec_fourcell
- Return type: int
- Signature: gpiochip_populate_parent_fwspec_fourcell(struct gpio_chip * gc,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 1887

### gpiochip_populate_parent_fwspec_twocell
- Return type: int
- Signature: gpiochip_populate_parent_fwspec_twocell(struct gpio_chip * gc,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 1871

### gpiochip_query_valid_mask
- Return type: const unsigned long *
- Signature: gpiochip_query_valid_mask(const struct gpio_chip * gc)
- Line: 808
- Called by: gpio_rcar_enable_inputs

### gpiochip_relres_irq
- Return type: void
- Signature: gpiochip_relres_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4291
- Calls: gpiochip_unlock_as_irq
- Called by: bcm_kona_gpio_irq_relres, gpiochip_irq_relres, rockchip_irq_relres, tegra_gpio_irq_release_resources, zynq_gpio_irq_relres

### gpiochip_remove
- Return type: void
- Signature: gpiochip_remove(struct gpio_chip * gc)
- Line: 1376
- Calls: acpi_gpiochip_remove, gpio_device_put, gpio_device_teardown_shared, gpiochip_free_hogs, gpiochip_free_remaining_irqs, gpiochip_free_valid_mask, gpiochip_irqchip_remove, gpiochip_remove_pin_ranges, gpiochip_set_data, gpiochip_sysfs_unregister, of_gpiochip_remove
- Called by: amd_gpio_exit, brcmstb_gpio_remove, bt8xxgpio_remove, devm_gpio_chip_release, gpio_rcar_probe, gpio_rcar_remove, gpio_regmap_register, gpio_regmap_unregister, it87_gpio_exit, ljca_gpio_remove, max3191x_remove, mb86s70_gpio_remove, mc33880_remove, omap_gpio_chip_init, omap_gpio_remove, rockchip_gpio_remove, rockchip_gpiolib_register, virtio_gpio_remove, zynq_gpio_remove

### gpiochip_remove_pin_ranges
- Return type: void
- Signature: gpiochip_remove_pin_ranges(struct gpio_chip * gc)
- Line: 2533
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpiochip_reqres_irq
- Return type: int
- Signature: gpiochip_reqres_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4274
- Calls: gpiochip_lock_as_irq
- Called by: bcm_kona_gpio_irq_reqres, gpiochip_irq_reqres, rockchip_irq_reqres, tegra_gpio_irq_request_resources, zynq_gpio_irq_reqres

### gpiochip_request_own_desc
- Return type: gpio_desc *
- Signature: gpiochip_request_own_desc(struct gpio_chip * gc,unsigned int hwnum,const char * label,enum gpio_lookup_flags lflags,enum gpiod_flags dflags)
- Line: 2722
- Calls: function_name_or_default, gpiochip_get_desc, gpiod_configure_flags, gpiod_free_commit, gpiod_line_state_notify, gpiod_request_commit
- Called by: acpi_request_own_gpiod, gpio_twl4030_probe, gpiod_hog, mvebu_pwm_request

### gpiochip_set
- Return type: static int
- Signature: gpiochip_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 3006
- Called by: gpiochip_set_multiple, gpiod_direction_output_raw_commit, gpiod_set_raw_value_commit

### gpiochip_set_data
- Return type: static void
- Signature: gpiochip_set_data(struct gpio_chip * gc,void * data)
- Line: 1069
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpiochip_set_desc_names
- Return type: static void
- Signature: gpiochip_set_desc_names(struct gpio_chip * gc)
- Line: 587
- Calls: gpio_name_to_desc
- Called by: gpiochip_add_data_with_key

### gpiochip_set_hierarchical_irqchip
- Return type: static void
- Signature: gpiochip_set_hierarchical_irqchip(struct gpio_chip * gc,struct irq_chip * irqchip)
- Line: 1611
- Called by: gpiochip_hierarchy_create_domain

### gpiochip_set_irq_hooks
- Return type: static void
- Signature: gpiochip_set_irq_hooks(struct gpio_chip * gc)
- Line: 2103
- Called by: gpiochip_add_irqchip

### gpiochip_set_multiple
- Return type: static int
- Signature: gpiochip_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 3777
- Calls: gpiochip_set
- Called by: gpiod_set_array_value_complex

### gpiochip_set_names
- Return type: static int
- Signature: gpiochip_set_names(struct gpio_chip * chip)
- Line: 617
- Called by: gpiochip_add_data_with_key

### gpiochip_setup_dev
- Return type: static int
- Signature: gpiochip_setup_dev(struct gpio_chip * gc)
- Line: 905
- Calls: gpiochip_sysfs_register
- Called by: gpiochip_add_data_with_key, gpiochip_setup_devs

### gpiochip_setup_devs
- Return type: static void
- Signature: gpiochip_setup_devs(void)
- Line: 1042
- Calls: gpio_device_put, gpiochip_setup_dev
- Called by: gpiolib_dev_init

### gpiochip_simple_create_domain
- Return type: static irq_domain *
- Signature: gpiochip_simple_create_domain(struct gpio_chip * gc)
- Line: 2003
- Called by: gpiochip_add_irqchip

### gpiochip_to_irq
- Return type: static int
- Signature: gpiochip_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 2016
- Calls: gpiochip_irqchip_irq_valid

### gpiochip_unlock_as_irq
- Return type: void
- Signature: gpiochip_unlock_as_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 4225
- Calls: gpiochip_get_desc
- Called by: acpi_gpiochip_alloc_event, acpi_gpiochip_free_interrupts, em_gio_irq_relres, gpio_sim_irq_released, gpio_sysfs_free_irq, gpio_sysfs_request_irq, gpiochip_irq_domain_deactivate, gpiochip_relres_irq, tegra_gpio_irq_shutdown, uniphier_gpio_irq_domain_deactivate, xgene_gpio_sb_domain_deactivate

### gpiod_add_lookup_table
- Return type: void
- Signature: gpiod_add_lookup_table(struct gpiod_lookup_table * table)
- Line: 4553
- Calls: gpiod_add_lookup_tables
- Called by: gpio_aggregator_activate, gpio_aggregator_new_device_store, gpio_shared_add_proxy_lookup, gpio_virtuser_make_lookup_table

### gpiod_add_lookup_tables
- Return type: void
- Signature: gpiod_add_lookup_tables(struct gpiod_lookup_table ** tables,size_t n)
- Line: 4503
- Called by: gpiod_add_lookup_table

### gpiod_cansleep
- Return type: int
- Signature: gpiod_cansleep(const struct gpio_desc * desc)
- Line: 4071
- Called by: gpio_la_poll_probe, gpio_latch_can_sleep, gpiochip_fwd_desc_add, gpiod_shared_desc_create

### gpiod_configure_flags
- Return type: int
- Signature: gpiod_configure_flags(struct gpio_desc * desc,const char * con_id,unsigned long lflags,enum gpiod_flags dflags)
- Line: 4964
- Calls: function_name_or_default, gpiod_direction_input_nonotify, gpiod_direction_output_nonotify, gpiod_set_transitory
- Called by: acpi_dev_gpio_irq_wake_get_by, gpiochip_request_own_desc, gpiod_find_and_request

### gpiod_count
- Return type: int
- Signature: gpiod_count(struct device * dev,const char * con_id)
- Line: 4890
- Calls: acpi_gpio_count, of_gpio_count, platform_gpio_count, swnode_gpio_count
- Called by: devm_gpiod_get_array_optional_count, gpio_aggregator_probe, gpiod_get_array

### gpiod_direction_input
- Return type: int
- Signature: gpiod_direction_input(struct gpio_desc * desc)
- Line: 2941
- Calls: gpiod_direction_input_nonotify, gpiod_line_state_notify
- Called by: direction_store, gpio_fwd_direction_input, gpio_shared_proxy_direction_input, gpio_virtuser_set_direction, lineevent_create

### gpiod_direction_input_nonotify
- Return type: int
- Signature: gpiod_direction_input_nonotify(struct gpio_desc * desc)
- Line: 2955
- Calls: desc_to_gpio, gpio_set_bias, gpiochip_direction_input, gpiochip_get_direction, gpiod_hwgpio
- Called by: gpiod_configure_flags, gpiod_direction_input, gpiod_direction_output_nonotify, linehandle_create, linehandle_set_config, linereq_create, linereq_set_config

### gpiod_direction_output
- Return type: int
- Signature: gpiod_direction_output(struct gpio_desc * desc,int value)
- Line: 3115
- Calls: gpiod_direction_output_nonotify, gpiod_line_state_notify
- Called by: gpio_fwd_direction_output, gpio_shared_proxy_direction_output, gpio_virtuser_set_direction

### gpiod_direction_output_nonotify
- Return type: int
- Signature: gpiod_direction_output_nonotify(struct gpio_desc * desc,int value)
- Line: 3129
- Calls: gpio_set_bias, gpio_set_config, gpiod_direction_input_nonotify, gpiod_direction_output_raw_commit
- Called by: gpiod_configure_flags, gpiod_direction_output, linehandle_create, linehandle_set_config, linereq_create, linereq_set_config

### gpiod_direction_output_raw
- Return type: int
- Signature: gpiod_direction_output_raw(struct gpio_desc * desc,int value)
- Line: 3088
- Calls: gpiod_direction_output_raw_commit, gpiod_line_state_notify
- Called by: direction_store

### gpiod_direction_output_raw_commit
- Return type: static int
- Signature: gpiod_direction_output_raw_commit(struct gpio_desc * desc,int value)
- Line: 3022
- Calls: desc_to_gpio, gpiochip_direction_output, gpiochip_get_direction, gpiochip_set, gpiod_hwgpio
- Called by: gpiod_direction_output_nonotify, gpiod_direction_output_raw

### gpiod_disable_hw_timestamp_ns
- Return type: int
- Signature: gpiod_disable_hw_timestamp_ns(struct gpio_desc * desc,unsigned long flags)
- Line: 3232
- Calls: gpiod_hwgpio

### gpiod_enable_hw_timestamp_ns
- Return type: int
- Signature: gpiod_enable_hw_timestamp_ns(struct gpio_desc * desc,unsigned long flags)
- Line: 3199
- Calls: gpiod_hwgpio

### gpiod_find
- Return type: static gpio_desc *
- Signature: gpiod_find(struct device * dev,const char * con_id,unsigned int idx,unsigned long * flags)
- Line: 4666
- Calls: gpio_desc_table_match, gpiod_match_lookup_table
- Called by: gpiod_find_and_request

### gpiod_find_and_request
- Return type: gpio_desc *
- Signature: gpiod_find_and_request(struct device * consumer,struct fwnode_handle * fwnode,const char * con_id,unsigned int idx,enum gpiod_flags flags,const char * label,bool platform_lookup_allowed)
- Line: 4756
- Calls: function_name_or_default, gpio_shared_add_proxy_lookup, gpiod_configure_flags, gpiod_find, gpiod_fwnode_lookup, gpiod_line_state_notify, gpiod_put, gpiod_request
- Called by: devm_fwnode_gpiod_get_index, fwnode_gpiod_get_index, gpiod_get_index

### gpiod_find_by_fwnode
- Return type: static gpio_desc *
- Signature: gpiod_find_by_fwnode(struct fwnode_handle * fwnode,struct device * consumer,const char * con_id,unsigned int idx,enum gpiod_flags * flags,unsigned long * lookupflags)
- Line: 4715
- Calls: acpi_find_gpio, function_name_or_default, of_find_gpio, swnode_find_gpio
- Called by: gpiod_fwnode_lookup

### gpiod_free
- Return type: void
- Signature: gpiod_free(struct gpio_desc * desc)
- Line: 2653
- Calls: gpio_device_put, gpiod_free_commit
- Called by: export_gpio_desc, gpio_free, gpiochip_sysfs_unregister, gpiod_put, lineevent_free, linehandle_free, linereq_free, unexport_gpio_desc

### gpiod_free_commit
- Return type: void
- Signature: gpiod_free_commit(struct gpio_desc * desc)
- Line: 2617
- Calls: desc_set_label, gpiod_hwgpio, gpiod_line_state_notify
- Called by: gpio_device_teardown_shared, gpiochip_free_own_desc, gpiochip_request_own_desc, gpiochip_setup_shared, gpiod_free

### gpiod_free_irqs
- Return type: static void
- Signature: gpiod_free_irqs(struct gpio_desc * desc)
- Line: 830
- Calls: gpiod_to_irq
- Called by: gpiochip_free_remaining_irqs

### gpiod_fwnode_lookup
- Return type: static gpio_desc *
- Signature: gpiod_fwnode_lookup(struct fwnode_handle * fwnode,struct device * consumer,const char * con_id,unsigned int idx,enum gpiod_flags * flags,unsigned long * lookupflags)
- Line: 4739
- Calls: gpiod_find_by_fwnode
- Called by: gpiod_find_and_request

### gpiod_get
- Return type: gpio_desc * __must_check
- Signature: gpiod_get(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 4920
- Calls: gpiod_get_index

### gpiod_get_array
- Return type: gpio_descs * __must_check
- Signature: gpiod_get_array(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 5157
- Calls: gpiod_count, gpiod_get_index, gpiod_hwgpio, gpiod_is_active_low, gpiod_put_array, gpiod_to_gpio_device
- Called by: devm_gpiod_get_array, gpiod_get_array_optional

### gpiod_get_array_optional
- Return type: gpio_descs * __must_check
- Signature: gpiod_get_array_optional(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 5290
- Calls: gpiod_get_array

### gpiod_get_array_value
- Return type: int
- Signature: gpiod_get_array_value(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 3681
- Calls: gpiod_get_array_value_complex
- Called by: gpio_fwd_get_multiple, gpio_la_get_array, gpio_virtuser_get_value_array_atomic

### gpiod_get_array_value_cansleep
- Return type: int
- Signature: gpiod_get_array_value_cansleep(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 4414
- Calls: gpiod_get_array_value_complex
- Called by: gpio_fwd_get_multiple, gpio_virtuser_get_array_value

### gpiod_get_array_value_complex
- Return type: int
- Signature: gpiod_get_array_value_complex(bool raw,bool can_sleep,unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 3464
- Calls: desc_to_gpio, gpio_chip_get_multiple, gpio_device_chip_cmp, gpiod_hwgpio
- Called by: gpiod_get_array_value, gpiod_get_array_value_cansleep, gpiod_get_raw_array_value, gpiod_get_raw_array_value_cansleep, linehandle_ioctl, linereq_get_values

### gpiod_get_direction
- Return type: int
- Signature: gpiod_get_direction(struct gpio_desc * desc)
- Line: 451
- Calls: gpiochip_get_direction, gpiod_hwgpio, validate_desc
- Called by: direction_show, gpio_fwd_get_direction, gpio_shared_proxy_direction_input, gpio_shared_proxy_direction_output, gpio_shared_proxy_get_direction, gpio_virtuser_direction_do_read, gpio_virtuser_do_get_direction_atomic, gpiochip_lock_as_irq, gpiod_request_commit, gpiolib_dbg_show

### gpiod_get_index
- Return type: gpio_desc * __must_check
- Signature: gpiod_get_index(struct device * dev,const char * con_id,unsigned int idx,enum gpiod_flags flags)
- Line: 5040
- Calls: gpiod_find_and_request
- Called by: devm_gpiod_get_index, gpiod_get, gpiod_get_array, gpiod_get_index_optional

### gpiod_get_index_optional
- Return type: gpio_desc * __must_check
- Signature: gpiod_get_index_optional(struct device * dev,const char * con_id,unsigned int index,enum gpiod_flags flags)
- Line: 5070
- Calls: gpiod_get_index
- Called by: gpiod_get_optional

### gpiod_get_label
- Return type: const char *
- Signature: gpiod_get_label(struct gpio_desc * desc)
- Line: 119
- Called by: gpio_desc_to_lineinfo, gpiochip_dup_line_label, gpiolib_dbg_show

### gpiod_get_optional
- Return type: gpio_desc * __must_check
- Signature: gpiod_get_optional(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 4942
- Calls: gpiod_get_index_optional

### gpiod_get_raw_array_value
- Return type: int
- Signature: gpiod_get_raw_array_value(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 3652
- Calls: gpiod_get_array_value_complex

### gpiod_get_raw_array_value_cansleep
- Return type: int
- Signature: gpiod_get_raw_array_value_cansleep(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 4385
- Calls: gpiod_get_array_value_complex

### gpiod_get_raw_value
- Return type: int
- Signature: gpiod_get_raw_value(const struct gpio_desc * desc)
- Line: 3597
- Calls: gpiod_get_raw_value_commit

### gpiod_get_raw_value_cansleep
- Return type: int
- Signature: gpiod_get_raw_value_cansleep(const struct gpio_desc * desc)
- Line: 4335
- Calls: gpiod_get_raw_value_commit
- Called by: acpi_gpio_adr_space_handler, acpi_gpiochip_request_irq, debounce_setup, debounce_work_func, gpio_lmux_gpio_get, process_hw_ts_thread

### gpiod_get_raw_value_commit
- Return type: static int
- Signature: gpiod_get_raw_value_commit(const struct gpio_desc * desc)
- Line: 3407
- Calls: desc_to_gpio, gpio_chip_get_value
- Called by: gpiod_get_raw_value, gpiod_get_raw_value_cansleep, gpiod_get_value, gpiod_get_value_cansleep

### gpiod_get_value
- Return type: int
- Signature: gpiod_get_value(const struct gpio_desc * desc)
- Line: 3617
- Calls: gpiod_get_raw_value_commit
- Called by: gpio_fwd_get, gpio_shared_proxy_get, gpio_virtuser_get_value_atomic

### gpiod_get_value_cansleep
- Return type: int
- Signature: gpiod_get_value_cansleep(const struct gpio_desc * desc)
- Line: 4353
- Calls: gpiod_get_raw_value_commit
- Called by: edge_irq_thread, gpio_fwd_get, gpio_shared_proxy_get_cansleep, gpio_virtuser_value_get, lineevent_ioctl, lineevent_irq_thread, max3191x_readout_locked, value_show

### gpiod_hog
- Return type: int
- Signature: gpiod_hog(struct gpio_desc * desc,const char * name,unsigned long lflags,enum gpiod_flags dflags)
- Line: 5096
- Calls: gpiochip_request_own_desc, gpiod_hwgpio
- Called by: gpiochip_add_hog

### gpiod_hwgpio
- Return type: int
- Signature: gpiod_hwgpio(const struct gpio_desc * desc)
- Line: 244
- Called by: aspeed_gpio_copro_grab_gpio, aspeed_gpio_copro_release_gpio, debounce_work_func, devm_gpiod_shared_get, edge_irq_thread, export_gpio_desc, gpio_chip_get_value, gpio_desc_to_lineinfo, gpio_do_set_config, gpio_set_config_with_argument_optional, gpio_set_open_drain_value_commit, gpio_set_open_source_value_commit, gpio_sysfs_free_irq, gpio_sysfs_request_irq, gpiod_direction_input_nonotify, gpiod_direction_output_raw_commit, gpiod_disable_hw_timestamp_ns, gpiod_enable_hw_timestamp_ns, gpiod_export, gpiod_free_commit, gpiod_get_array, gpiod_get_array_value_complex, gpiod_get_direction, gpiod_hog, gpiod_request_commit, gpiod_set_array_value_complex, gpiod_set_raw_value_commit, gpiod_to_irq, lineinfo_changed_notify, linereq_show_fdinfo, process_hw_ts_thread

### gpiod_is_active_low
- Return type: int
- Signature: gpiod_is_active_low(const struct gpio_desc * desc)
- Line: 3343
- Called by: gpio_fwd_delay, gpiod_get_array

### gpiod_is_equal
- Return type: bool
- Signature: gpiod_is_equal(const struct gpio_desc * desc,const struct gpio_desc * other)
- Line: 416
- Calls: validate_desc
- Called by: gpiod_unexport_unlocked, match_export

### gpiod_is_shared
- Return type: bool
- Signature: gpiod_is_shared(const struct gpio_desc * desc)
- Line: 4114

### gpiod_line_state_notify
- Return type: void
- Signature: gpiod_line_state_notify(struct gpio_desc * desc,unsigned long action)
- Line: 4542
- Called by: edge_store, export_gpio_desc, gpio_set_debounce_timeout, gpio_sysfs_set_active_low, gpiochip_request_own_desc, gpiod_direction_input, gpiod_direction_output, gpiod_direction_output_raw, gpiod_find_and_request, gpiod_free_commit, gpiod_set_config, gpiod_set_consumer_name, gpiod_toggle_active_low, lineevent_create, linehandle_create, linehandle_set_config, linereq_create, linereq_set_config

### gpiod_match_lookup_table
- Return type: static bool
- Signature: gpiod_match_lookup_table(struct device * dev,const struct gpiod_lookup_table * table)
- Line: 4575
- Called by: gpiod_find, platform_gpio_count

### gpiod_put
- Return type: void
- Signature: gpiod_put(struct gpio_desc * desc)
- Line: 5310
- Calls: gpiod_free
- Called by: devm_gpiod_release, gpiochip_fwd_desc_free, gpiod_find_and_request, gpiod_put_array

### gpiod_put_array
- Return type: void
- Signature: gpiod_put_array(struct gpio_descs * descs)
- Line: 5320
- Calls: gpiod_put
- Called by: devm_gpiod_release_array, gpiod_get_array

### gpiod_remove_lookup_table
- Return type: void
- Signature: gpiod_remove_lookup_table(struct gpiod_lookup_table * table)
- Line: 4563
- Called by: gpio_aggregator_activate, gpio_aggregator_deactivate, gpio_aggregator_new_device_store, gpio_device_teardown_shared, gpio_virtuser_remove_lookup_table

### gpiod_request
- Return type: int
- Signature: gpiod_request(struct gpio_desc * desc,const char * label)
- Line: 2597
- Calls: gpio_device_get, gpiod_request_commit
- Called by: gpio_request, gpiod_find_and_request

### gpiod_request_commit
- Return type: int
- Signature: gpiod_request_commit(struct gpio_desc * desc,const char * label)
- Line: 2553
- Calls: desc_set_label, gpiochip_line_is_valid, gpiod_get_direction, gpiod_hwgpio
- Called by: gpiochip_request_own_desc, gpiochip_setup_shared, gpiod_request

### gpiod_set_array_value
- Return type: int
- Signature: gpiod_set_array_value(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 4051
- Calls: gpiod_set_array_value_complex
- Called by: gpio_fwd_set_multiple, gpio_virtuser_set_value_array_atomic

### gpiod_set_array_value_cansleep
- Return type: int
- Signature: gpiod_set_array_value_cansleep(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 4528
- Calls: gpiod_set_array_value_complex
- Called by: gpio_fwd_set_multiple

### gpiod_set_array_value_complex
- Return type: int
- Signature: gpiod_set_array_value_complex(bool raw,bool can_sleep,unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 3803
- Calls: desc_to_gpio, gpio_device_chip_cmp, gpio_set_open_drain_value_commit, gpio_set_open_source_value_commit, gpiochip_set_multiple, gpiod_hwgpio
- Called by: gpiod_set_array_value, gpiod_set_array_value_cansleep, gpiod_set_raw_array_value, gpiod_set_raw_array_value_cansleep, linehandle_ioctl, linereq_set_values

### gpiod_set_config
- Return type: int
- Signature: gpiod_set_config(struct gpio_desc * desc,unsigned long config)
- Line: 3266
- Calls: gpio_do_set_config, gpiod_line_state_notify
- Called by: gpio_fwd_set_config, gpio_shared_proxy_set_config, gpiod_set_debounce

### gpiod_set_consumer_name
- Return type: int
- Signature: gpiod_set_consumer_name(struct gpio_desc * desc,const char * name)
- Line: 4086
- Calls: desc_set_label, gpiod_line_state_notify
- Called by: acpi_dev_gpio_irq_wake_get_by, gpio_la_poll_probe, gpio_virtuser_consumer_write

### gpiod_set_debounce
- Return type: int
- Signature: gpiod_set_debounce(struct gpio_desc * desc,unsigned int debounce)
- Line: 3304
- Calls: gpiod_set_config
- Called by: gpio_virtuser_debounce_set

### gpiod_set_raw_array_value
- Return type: int
- Signature: gpiod_set_raw_array_value(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 4023
- Calls: gpiod_set_array_value_complex

### gpiod_set_raw_array_value_cansleep
- Return type: int
- Signature: gpiod_set_raw_array_value_cansleep(unsigned int array_size,struct gpio_desc ** desc_array,struct gpio_array * array_info,unsigned long * value_bitmap)
- Line: 4485
- Calls: gpiod_set_array_value_complex

### gpiod_set_raw_value
- Return type: int
- Signature: gpiod_set_raw_value(struct gpio_desc * desc,int value)
- Line: 3950
- Calls: gpiod_set_raw_value_commit

### gpiod_set_raw_value_cansleep
- Return type: int
- Signature: gpiod_set_raw_value_cansleep(struct gpio_desc * desc,int value)
- Line: 4441
- Calls: gpiod_set_raw_value_commit
- Called by: acpi_gpio_adr_space_handler

### gpiod_set_raw_value_commit
- Return type: static int
- Signature: gpiod_set_raw_value_commit(struct gpio_desc * desc,bool value)
- Line: 3752
- Calls: desc_to_gpio, gpiochip_set, gpiod_hwgpio
- Called by: gpiod_set_raw_value, gpiod_set_raw_value_cansleep, gpiod_set_value_nocheck

### gpiod_set_transitory
- Return type: int
- Signature: gpiod_set_transitory(struct gpio_desc * desc,bool transitory)
- Line: 3321
- Calls: gpio_set_config_with_argument_optional
- Called by: export_gpio_desc, gpiod_configure_flags, linehandle_create, linereq_create

### gpiod_set_value
- Return type: int
- Signature: gpiod_set_value(struct gpio_desc * desc,int value)
- Line: 3998
- Calls: gpiod_set_value_nocheck
- Called by: gpio_fwd_set, gpio_virtuser_set_value_atomic

### gpiod_set_value_cansleep
- Return type: int
- Signature: gpiod_set_value_cansleep(struct gpio_desc * desc,int value)
- Line: 4462
- Calls: gpiod_set_value_nocheck
- Called by: gen_74x164_activate, gen_74x164_deactivate, gpio_fwd_set, gpio_virtuser_value_set, max3191x_set_config, pcf857x_probe, pisosr_gpio_refresh, value_store

### gpiod_set_value_nocheck
- Return type: static int
- Signature: gpiod_set_value_nocheck(struct gpio_desc * desc,int value)
- Line: 3971
- Calls: gpio_set_open_drain_value_commit, gpio_set_open_source_value_commit, gpiod_set_raw_value_commit
- Called by: gpiod_set_value, gpiod_set_value_cansleep

### gpiod_to_chip
- Return type: gpio_chip *
- Signature: gpiod_to_chip(const struct gpio_desc * desc)
- Line: 262
- Calls: gpio_device_get_chip
- Called by: aspeed_gpio_copro_grab_gpio, aspeed_gpio_copro_release_gpio

### gpiod_to_gpio_device
- Return type: gpio_device *
- Signature: gpiod_to_gpio_device(struct gpio_desc * desc)
- Line: 283
- Called by: gpiod_get_array, gpiod_unexport_unlocked

### gpiod_to_irq
- Return type: int
- Signature: gpiod_to_irq(const struct gpio_desc * desc)
- Line: 4127
- Calls: gpiod_hwgpio, validate_desc
- Called by: acpi_dev_gpio_irq_wake_get_by, acpi_gpiochip_alloc_event, debounce_setup, edge_detector_setup, gpio_fwd_to_irq, gpio_is_visible, gpio_shared_proxy_to_irq, gpio_sysfs_request_irq, gpio_virtuser_interrupts_set, gpiochip_fwd_desc_add, gpiod_free_irqs, lineevent_create

### gpiod_toggle_active_low
- Return type: void
- Signature: gpiod_toggle_active_low(struct gpio_desc * desc)
- Line: 3354
- Calls: gpiod_line_state_notify

### gpiodev_add_to_list_unlocked
- Return type: static int
- Signature: gpiodev_add_to_list_unlocked(struct gpio_device * gdev)
- Line: 501
- Called by: gpiochip_add_data_with_key

### gpiodev_release
- Return type: static void
- Signature: gpiodev_release(struct device * dev)
- Line: 869

### gpiolib_dbg_show
- Return type: static void
- Signature: gpiolib_dbg_show(struct seq_file * s,struct gpio_chip * gc)
- Line: 5387
- Calls: gpio_chip_get_value, gpiod_get_direction, gpiod_get_label
- Called by: gpiolib_seq_show

### gpiolib_debugfs_init
- Return type: static int __init
- Signature: gpiolib_debugfs_init(void)
- Line: 5520

### gpiolib_dev_init
- Return type: static int __init
- Signature: gpiolib_dev_init(void)
- Line: 5348
- Calls: gpiochip_setup_devs

### gpiolib_seq_next
- Return type: static void *
- Signature: gpiolib_seq_next(struct seq_file * s,void * v,loff_t * pos)
- Line: 5449

### gpiolib_seq_show
- Return type: static int
- Signature: gpiolib_seq_show(struct seq_file * s,void * v)
- Line: 5474
- Calls: gpiolib_dbg_show

### gpiolib_seq_start
- Return type: static void *
- Signature: gpiolib_seq_start(struct seq_file * s,loff_t * pos)
- Line: 5423

### gpiolib_seq_stop
- Return type: static void
- Signature: gpiolib_seq_stop(struct seq_file * s,void * v)
- Line: 5462

### platform_gpio_count
- Return type: static int
- Signature: platform_gpio_count(struct device * dev,const char * con_id)
- Line: 4689
- Calls: gpiod_match_lookup_table
- Called by: gpiod_count

### validate_desc
- Return type: static int
- Signature: validate_desc(const struct gpio_desc * desc,const char * func)
- Line: 383
- Called by: gpiod_get_direction, gpiod_is_equal, gpiod_to_irq

## Structs (1)

### gpiolib_seq_priv
- Line: 5418
- Members:
  - newline: bool
  - idx: int

## Variables (8)

- static **gpio_bus_type** : const struct bus_type (line 74)
- static **gpio_dev_type** : const struct device_type (line 884)
- static **gpio_devt** : dev_t (line 58)
- static **gpio_stub_drv** : device_driver (line 5343)
- **gpio_suffixes** : const char * const[] (line 106)
- static **gpiochip_domain_ops** : const struct irq_domain_ops (line 1995)
- static **gpiolib_initialized** : bool (line 117)
- static **gpiolib_sops** : const struct seq_operations (line 5512)

## Macros (11)

- **CREATE_TRACE_POINTS** (line 46)
- **FASTPATH_NGPIO** (line 95)
- **GPIO_DEV_MAX** (line 59)
- **GPIO_DYNAMIC_BASE** (line 84)
- **GPIO_DYNAMIC_MAX** (line 90)
- **VALIDATE_DESC**(desc) (line 396)
- **VALIDATE_DESC_VOID**(desc) (line 402)
- **gcdev_register**(gc,devt) (line 890)
- **gcdev_register**(gc,devt) (line 897)
- **gcdev_unregister**(gdev) (line 891)
- **gcdev_unregister**(gdev) (line 898)
