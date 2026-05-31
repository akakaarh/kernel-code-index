# drivers/gpio/gpio-tegra186.c

Subsystem: drivers/gpio

## Functions (29)

### tegra186_gpio_add_pin_ranges
- Return type: static int
- Signature: tegra186_gpio_add_pin_ranges(struct gpio_chip * chip)
- Line: 451
- Calls: gpiochip_add_pingroup_range, gpiochip_get_data

### tegra186_gpio_child_offset_to_irq
- Return type: static unsigned int
- Signature: tegra186_gpio_child_offset_to_irq(struct gpio_chip * chip,unsigned int offset)
- Line: 759
- Calls: gpiochip_get_data

### tegra186_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: tegra186_gpio_child_to_parent_hwirq(struct gpio_chip * chip,unsigned int hwirq,unsigned int type,unsigned int * parent_hwirq,unsigned int * parent_type)
- Line: 747

### tegra186_gpio_direction_input
- Return type: static int
- Signature: tegra186_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 273
- Calls: gpiochip_get_data, tegra186_gpio_get_base

### tegra186_gpio_direction_output
- Return type: static int
- Signature: tegra186_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int level)
- Line: 296
- Calls: gpiochip_get_data, tegra186_gpio_get_base, tegra186_gpio_set

### tegra186_gpio_dis_hw_ts
- Return type: static int
- Signature: tegra186_gpio_dis_hw_ts(struct gpio_chip * gc,u32 offset,unsigned long flags)
- Line: 363
- Calls: gpiochip_get_data, tegra186_gpio_get_base

### tegra186_gpio_en_hw_ts
- Return type: static int
- Signature: tegra186_gpio_en_hw_ts(struct gpio_chip * gc,u32 offset,unsigned long flags)
- Line: 328
- Calls: gpiochip_get_data, tegra186_gpio_get_base

### tegra186_gpio_get
- Return type: static int
- Signature: tegra186_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 396
- Calls: gpiochip_get_data, tegra186_gpio_get_base

### tegra186_gpio_get_base
- Return type: static void __iomem *
- Signature: tegra186_gpio_get_base(struct tegra_gpio * gpio,unsigned int pin)
- Line: 158
- Calls: tegra186_gpio_get_port
- Called by: tegra186_gpio_direction_input, tegra186_gpio_direction_output, tegra186_gpio_dis_hw_ts, tegra186_gpio_en_hw_ts, tegra186_gpio_get, tegra186_gpio_get_direction, tegra186_gpio_set, tegra186_gpio_set_config, tegra186_irq_ack, tegra186_irq_mask, tegra186_irq_set_type, tegra186_irq_unmask

### tegra186_gpio_get_direction
- Return type: static int
- Signature: tegra186_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 255
- Calls: gpiochip_get_data, tegra186_gpio_get_base

### tegra186_gpio_get_port
- Return type: static const struct tegra_gpio_port *
- Signature: tegra186_gpio_get_port(struct tegra_gpio * gpio,unsigned int * pin)
- Line: 140
- Called by: tegra186_gpio_get_base, tegra186_gpio_get_secure_base

### tegra186_gpio_get_secure_base
- Return type: static void __iomem *
- Signature: tegra186_gpio_get_secure_base(struct tegra_gpio * gpio,unsigned int pin)
- Line: 173
- Calls: tegra186_gpio_get_port
- Called by: tegra186_gpio_is_accessible

### tegra186_gpio_init_route_mapping
- Return type: static void
- Signature: tegra186_gpio_init_route_mapping(struct tegra_gpio * gpio)
- Line: 782
- Called by: tegra186_gpio_probe

### tegra186_gpio_irq
- Return type: static void
- Signature: tegra186_gpio_irq(struct irq_desc * desc)
- Line: 660

### tegra186_gpio_irq_domain_translate
- Return type: static int
- Signature: tegra186_gpio_irq_domain_translate(struct irq_domain * domain,struct irq_fwspec * fwspec,unsigned long * hwirq,unsigned int * type)
- Line: 701
- Calls: gpiochip_get_data

### tegra186_gpio_irqs_per_bank
- Return type: static unsigned int
- Signature: tegra186_gpio_irqs_per_bank(struct tegra_gpio * gpio)
- Line: 828
- Called by: tegra186_gpio_probe

### tegra186_gpio_is_accessible
- Return type: static bool
- Signature: tegra186_gpio_is_accessible(struct tegra_gpio * gpio,unsigned int pin)
- Line: 188
- Calls: tegra186_gpio_get_secure_base
- Called by: tegra186_init_valid_mask

### tegra186_gpio_of_xlate
- Return type: static int
- Signature: tegra186_gpio_of_xlate(struct gpio_chip * chip,const struct of_phandle_args * spec,u32 * flags)
- Line: 495
- Calls: gpiochip_get_data

### tegra186_gpio_populate_parent_fwspec
- Return type: static int
- Signature: tegra186_gpio_populate_parent_fwspec(struct gpio_chip * chip,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 730
- Calls: gpiochip_get_data

### tegra186_gpio_probe
- Return type: static int
- Signature: tegra186_gpio_probe(struct platform_device * pdev)
- Line: 853
- Calls: tegra186_gpio_init_route_mapping, tegra186_gpio_irqs_per_bank

### tegra186_gpio_set
- Return type: static int
- Signature: tegra186_gpio_set(struct gpio_chip * chip,unsigned int offset,int level)
- Line: 233
- Calls: gpiochip_get_data, tegra186_gpio_get_base
- Called by: tegra186_gpio_direction_output

### tegra186_gpio_set_config
- Return type: static int
- Signature: tegra186_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 415
- Calls: gpiochip_get_data, tegra186_gpio_get_base

### tegra186_init_valid_mask
- Return type: static int
- Signature: tegra186_init_valid_mask(struct gpio_chip * chip,unsigned long * valid_mask,unsigned int ngpios)
- Line: 220
- Calls: gpiochip_get_data, tegra186_gpio_is_accessible

### tegra186_irq_ack
- Return type: static void
- Signature: tegra186_irq_ack(struct irq_data * data)
- Line: 527
- Calls: tegra186_gpio_get_base

### tegra186_irq_mask
- Return type: static void
- Signature: tegra186_irq_mask(struct irq_data * data)
- Line: 540
- Calls: gpiochip_disable_irq, tegra186_gpio_get_base

### tegra186_irq_print_chip
- Return type: static void
- Signature: tegra186_irq_print_chip(struct irq_data * data,struct seq_file * p)
- Line: 642

### tegra186_irq_set_type
- Return type: static int
- Signature: tegra186_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 576
- Calls: tegra186_gpio_get_base

### tegra186_irq_set_wake
- Return type: static int
- Signature: tegra186_irq_set_wake(struct irq_data * data,unsigned int on)
- Line: 634

### tegra186_irq_unmask
- Return type: static void
- Signature: tegra186_irq_unmask(struct irq_data * data)
- Line: 558
- Calls: gpiochip_enable_irq, tegra186_gpio_get_base

## Structs (4)

### tegra186_pin_range
- Line: 104
- Members:
  - name: const char *
  - bank: unsigned int
  - port: unsigned int
  - pins: unsigned int
  - offset: unsigned int
  - group: const char *
  - ports: const struct tegra_gpio_port *
  - num_ports: unsigned int
  - name: const char *
  - prefix: const char *
  - instance: unsigned int
  - num_irqs_per_bank: unsigned int
  - pin_ranges: const struct tegra186_pin_range *
  - num_pin_ranges: unsigned int
  - pinmux: const char *
  - has_gte: bool
  - has_vm_support: bool
  - gpio: gpio_chip
  - num_irq: unsigned int
  - soc: const struct tegra_gpio_soc *
  - num_irqs_per_bank: unsigned int
  - num_banks: unsigned int
  - secure: void __iomem *
  - base: void __iomem *

### tegra_gpio
- Line: 125
- Members:
  - name: const char *
  - bank: unsigned int
  - port: unsigned int
  - pins: unsigned int
  - offset: unsigned int
  - group: const char *
  - ports: const struct tegra_gpio_port *
  - num_ports: unsigned int
  - name: const char *
  - prefix: const char *
  - instance: unsigned int
  - num_irqs_per_bank: unsigned int
  - pin_ranges: const struct tegra186_pin_range *
  - num_pin_ranges: unsigned int
  - pinmux: const char *
  - has_gte: bool
  - has_vm_support: bool
  - gpio: gpio_chip
  - num_irq: unsigned int
  - soc: const struct tegra_gpio_soc *
  - num_irqs_per_bank: unsigned int
  - num_banks: unsigned int
  - secure: void __iomem *
  - base: void __iomem *

### tegra_gpio_port
- Line: 97
- Members:
  - name: const char *
  - bank: unsigned int
  - port: unsigned int
  - pins: unsigned int
  - offset: unsigned int
  - group: const char *
  - ports: const struct tegra_gpio_port *
  - num_ports: unsigned int
  - name: const char *
  - prefix: const char *
  - instance: unsigned int
  - num_irqs_per_bank: unsigned int
  - pin_ranges: const struct tegra186_pin_range *
  - num_pin_ranges: unsigned int
  - pinmux: const char *
  - has_gte: bool
  - has_vm_support: bool
  - gpio: gpio_chip
  - num_irq: unsigned int
  - soc: const struct tegra_gpio_soc *
  - num_irqs_per_bank: unsigned int
  - num_banks: unsigned int
  - secure: void __iomem *
  - base: void __iomem *

### tegra_gpio_soc
- Line: 109
- Members:
  - name: const char *
  - bank: unsigned int
  - port: unsigned int
  - pins: unsigned int
  - offset: unsigned int
  - group: const char *
  - ports: const struct tegra_gpio_port *
  - num_ports: unsigned int
  - name: const char *
  - prefix: const char *
  - instance: unsigned int
  - num_irqs_per_bank: unsigned int
  - pin_ranges: const struct tegra186_pin_range *
  - num_pin_ranges: unsigned int
  - pinmux: const char *
  - has_gte: bool
  - has_vm_support: bool
  - gpio: gpio_chip
  - num_irq: unsigned int
  - soc: const struct tegra_gpio_soc *
  - num_irqs_per_bank: unsigned int
  - num_banks: unsigned int
  - secure: void __iomem *
  - base: void __iomem *

## Variables (34)

- static **tegra186_aon_ports** : const struct tegra_gpio_port[] (line 1088)
- static **tegra186_aon_soc** : const struct tegra_gpio_soc (line 1099)
- static **tegra186_gpio_acpi_match** : const struct acpi_device_id[] (line 1468)
- static **tegra186_gpio_driver** : platform_driver (line 1481)
- static **tegra186_gpio_irq_chip** : const struct irq_chip (line 649)
- static **tegra186_gpio_of_match** : const struct of_device_id[] (line 1431)
- static **tegra186_main_ports** : const struct tegra_gpio_port[] (line 1050)
- static **tegra186_main_soc** : const struct tegra_gpio_soc (line 1076)
- static **tegra186_pmc_of_match** : const struct of_device_id[] (line 775)
- static **tegra194_aon_ports** : const struct tegra_gpio_port[] (line 1162)
- static **tegra194_aon_soc** : const struct tegra_gpio_soc (line 1170)
- static **tegra194_main_pin_ranges** : const struct tegra186_pin_range[] (line 1142)
- static **tegra194_main_ports** : const struct tegra_gpio_port[] (line 1111)
- static **tegra194_main_soc** : const struct tegra_gpio_soc (line 1147)
- static **tegra234_aon_ports** : const struct tegra_gpio_port[] (line 1223)
- static **tegra234_aon_soc** : const struct tegra_gpio_soc (line 1232)
- static **tegra234_main_ports** : const struct tegra_gpio_port[] (line 1183)
- static **tegra234_main_soc** : const struct tegra_gpio_soc (line 1211)
- static **tegra241_aon_ports** : const struct tegra_gpio_port[] (line 1271)
- static **tegra241_aon_soc** : const struct tegra_gpio_soc (line 1276)
- static **tegra241_main_ports** : const struct tegra_gpio_port[] (line 1245)
- static **tegra241_main_soc** : const struct tegra_gpio_soc (line 1259)
- static **tegra256_main_ports** : const struct tegra_gpio_port[] (line 1362)
- static **tegra256_main_soc** : const struct tegra_gpio_soc (line 1369)
- static **tegra264_aon_ports** : const struct tegra_gpio_port[] (line 1322)
- static **tegra264_aon_soc** : const struct tegra_gpio_soc (line 1330)
- static **tegra264_main_ports** : const struct tegra_gpio_port[] (line 1288)
- static **tegra264_main_soc** : const struct tegra_gpio_soc (line 1310)
- static **tegra264_uphy_ports** : const struct tegra_gpio_port[] (line 1342)
- static **tegra264_uphy_soc** : const struct tegra_gpio_soc (line 1350)
- static **tegra410_compute_ports** : const struct tegra_gpio_port[] (line 1384)
- static **tegra410_compute_soc** : const struct tegra_gpio_soc (line 1392)
- static **tegra410_system_ports** : const struct tegra_gpio_port[] (line 1404)
- static **tegra410_system_soc** : const struct tegra_gpio_soc (line 1422)

## Macros (73)

- **HTE_BOTH_EDGES** (line 326)
- **TEGRA186_AON_GPIO_PORT**(_name,_bank,_port,_pins) (line 1085)
- **TEGRA186_GPIO_CTL_SCR** (line 27)
- **TEGRA186_GPIO_CTL_SCR_SEC_REN** (line 29)
- **TEGRA186_GPIO_CTL_SCR_SEC_WEN** (line 28)
- **TEGRA186_GPIO_DEBOUNCE_CONTROL** (line 57)
- **TEGRA186_GPIO_DEBOUNCE_CONTROL_THRESHOLD**(x) (line 58)
- **TEGRA186_GPIO_ENABLE_CONFIG** (line 44)
- **TEGRA186_GPIO_ENABLE_CONFIG_DEBOUNCE** (line 53)
- **TEGRA186_GPIO_ENABLE_CONFIG_ENABLE** (line 45)
- **TEGRA186_GPIO_ENABLE_CONFIG_INTERRUPT** (line 54)
- **TEGRA186_GPIO_ENABLE_CONFIG_OUT** (line 46)
- **TEGRA186_GPIO_ENABLE_CONFIG_TIMESTAMP_FUNC** (line 55)
- **TEGRA186_GPIO_ENABLE_CONFIG_TRIGGER_LEVEL** (line 52)
- **TEGRA186_GPIO_ENABLE_CONFIG_TRIGGER_TYPE_DOUBLE_EDGE** (line 50)
- **TEGRA186_GPIO_ENABLE_CONFIG_TRIGGER_TYPE_LEVEL** (line 48)
- **TEGRA186_GPIO_ENABLE_CONFIG_TRIGGER_TYPE_MASK** (line 51)
- **TEGRA186_GPIO_ENABLE_CONFIG_TRIGGER_TYPE_NONE** (line 47)
- **TEGRA186_GPIO_ENABLE_CONFIG_TRIGGER_TYPE_SINGLE_EDGE** (line 49)
- **TEGRA186_GPIO_INPUT** (line 60)
- **TEGRA186_GPIO_INPUT_HIGH** (line 61)
- **TEGRA186_GPIO_INTERRUPT_CLEAR** (line 69)
- **TEGRA186_GPIO_INTERRUPT_STATUS**(x) (line 71)
- **TEGRA186_GPIO_INT_ROUTE_MAPPING**(p,x) (line 31)
- **TEGRA186_GPIO_OUTPUT_CONTROL** (line 63)
- **TEGRA186_GPIO_OUTPUT_CONTROL_FLOATED** (line 64)
- **TEGRA186_GPIO_OUTPUT_VALUE** (line 66)
- **TEGRA186_GPIO_OUTPUT_VALUE_HIGH** (line 67)
- **TEGRA186_GPIO_SCR** (line 35)
- **TEGRA186_GPIO_SCR_PIN_SIZE** (line 36)
- **TEGRA186_GPIO_SCR_PORT_SIZE** (line 37)
- **TEGRA186_GPIO_SCR_SEC_G1R** (line 41)
- **TEGRA186_GPIO_SCR_SEC_G1W** (line 40)
- **TEGRA186_GPIO_SCR_SEC_REN** (line 39)
- **TEGRA186_GPIO_SCR_SEC_WEN** (line 38)
- **TEGRA186_GPIO_VM** (line 33)
- **TEGRA186_GPIO_VM_RW_MASK** (line 34)
- **TEGRA186_MAIN_GPIO_PORT**(_name,_bank,_port,_pins) (line 1047)
- **TEGRA194_AON_GPIO_PORT**(_name,_bank,_port,_pins) (line 1159)
- **TEGRA194_MAIN_GPIO_PORT**(_name,_bank,_port,_pins) (line 1108)
- **TEGRA234_AON_GPIO_PORT**(_name,_bank,_port,_pins) (line 1220)
- **TEGRA234_MAIN_GPIO_PORT**(_name,_bank,_port,_pins) (line 1180)
- **TEGRA241_AON_GPIO_PORT**(_name,_bank,_port,_pins) (line 1268)
- **TEGRA241_MAIN_GPIO_PORT**(_name,_bank,_port,_pins) (line 1242)
- **TEGRA256_MAIN_GPIO_PORT**(_name,_bank,_port,_pins) (line 1359)
- **TEGRA264_AON_GPIO_PORT**(_name,_bank,_port,_pins) (line 1319)
- **TEGRA264_MAIN_GPIO_PORT**(_name,_bank,_port,_pins) (line 1285)
- **TEGRA264_UPHY_GPIO_PORT**(_name,_bank,_port,_pins) (line 1339)
- **TEGRA410_COMPUTE_GPIO_PORT**(_name,_bank,_port,_pins) (line 1381)
- **TEGRA410_COMPUTE_GPIO_PORT_A** (line 74)
- **TEGRA410_COMPUTE_GPIO_PORT_B** (line 75)
- **TEGRA410_COMPUTE_GPIO_PORT_C** (line 76)
- **TEGRA410_COMPUTE_GPIO_PORT_D** (line 77)
- **TEGRA410_COMPUTE_GPIO_PORT_E** (line 78)
- **TEGRA410_SYSTEM_GPIO_PORT**(_name,_bank,_port,_pins) (line 1401)
- **TEGRA410_SYSTEM_GPIO_PORT_A** (line 81)
- **TEGRA410_SYSTEM_GPIO_PORT_B** (line 82)
- **TEGRA410_SYSTEM_GPIO_PORT_C** (line 83)
- **TEGRA410_SYSTEM_GPIO_PORT_D** (line 84)
- **TEGRA410_SYSTEM_GPIO_PORT_E** (line 85)
- **TEGRA410_SYSTEM_GPIO_PORT_I** (line 86)
- **TEGRA410_SYSTEM_GPIO_PORT_J** (line 87)
- **TEGRA410_SYSTEM_GPIO_PORT_K** (line 88)
- **TEGRA410_SYSTEM_GPIO_PORT_L** (line 89)
- **TEGRA410_SYSTEM_GPIO_PORT_M** (line 90)
- **TEGRA410_SYSTEM_GPIO_PORT_N** (line 91)
- **TEGRA410_SYSTEM_GPIO_PORT_P** (line 92)
- **TEGRA410_SYSTEM_GPIO_PORT_Q** (line 93)
- **TEGRA410_SYSTEM_GPIO_PORT_R** (line 94)
- **TEGRA410_SYSTEM_GPIO_PORT_V** (line 95)
- **TEGRA_GPIO_PORT**(_prefix,_name,_bank,_port,_pins) (line 1039)
- **TEGRA_GPIO_PREFIX**(_x) (line 1379)
- **to_tegra_gpio**(x) (line 525)
