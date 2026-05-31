# drivers/gpio/gpio-dwapb.c

Subsystem: drivers/gpio

## Functions (31)

### dwapb_assert_reset
- Return type: static void
- Signature: dwapb_assert_reset(void * data)
- Line: 631

### dwapb_configure_irqs
- Return type: static void
- Signature: dwapb_configure_irqs(struct dwapb_gpio * gpio,struct dwapb_gpio_port * port,struct dwapb_port_property * pp)
- Line: 440
- Calls: dwapb_convert_irqs
- Called by: dwapb_gpio_add_port

### dwapb_convert_irqs
- Return type: static int
- Signature: dwapb_convert_irqs(struct dwapb_gpio_port_irqchip * pirq,struct dwapb_port_property * pp)
- Line: 424
- Called by: dwapb_configure_irqs

### dwapb_disable_clks
- Return type: static void
- Signature: dwapb_disable_clks(void * data)
- Line: 656

### dwapb_do_irq
- Return type: static u32
- Signature: dwapb_do_irq(struct dwapb_gpio * gpio)
- Line: 203
- Calls: dwapb_read, dwapb_toggle_trigger
- Called by: dwapb_irq_handler, dwapb_irq_handler_mfd

### dwapb_get_clks
- Return type: static int
- Signature: dwapb_get_clks(struct dwapb_gpio * gpio)
- Line: 663
- Called by: dwapb_gpio_probe

### dwapb_get_irq
- Return type: static void
- Signature: dwapb_get_irq(struct device * dev,struct fwnode_handle * fwnode,struct dwapb_port_property * pp)
- Line: 562
- Called by: dwapb_gpio_get_pdata

### dwapb_get_reset
- Return type: static int
- Signature: dwapb_get_reset(struct dwapb_gpio * gpio)
- Line: 638
- Called by: dwapb_gpio_probe

### dwapb_gpio_add_port
- Return type: static int
- Signature: dwapb_gpio_add_port(struct dwapb_gpio * gpio,struct dwapb_port_property * pp,unsigned int offs)
- Line: 497
- Calls: dwapb_configure_irqs, gpio_generic_chip_init
- Called by: dwapb_gpio_probe

### dwapb_gpio_get_pdata
- Return type: static dwapb_platform_data *
- Signature: dwapb_gpio_get_pdata(struct device * dev)
- Line: 577
- Calls: dwapb_get_irq
- Called by: dwapb_gpio_probe

### dwapb_gpio_probe
- Return type: static int
- Signature: dwapb_gpio_probe(struct platform_device * pdev)
- Line: 701
- Calls: dwapb_get_clks, dwapb_get_reset, dwapb_gpio_add_port, dwapb_gpio_get_pdata

### dwapb_gpio_resume
- Return type: static int
- Signature: dwapb_gpio_resume(struct device * dev)
- Line: 785
- Calls: dwapb_write

### dwapb_gpio_set_config
- Return type: static int
- Signature: dwapb_gpio_set_config(struct gpio_chip * gc,unsigned offset,unsigned long config)
- Line: 411
- Calls: dwapb_gpio_set_debounce, gpiochip_generic_config

### dwapb_gpio_set_debounce
- Return type: static int
- Signature: dwapb_gpio_set_debounce(struct gpio_chip * gc,unsigned offset,unsigned debounce)
- Line: 390
- Calls: dwapb_read, dwapb_write, gpiochip_get_data
- Called by: dwapb_gpio_set_config

### dwapb_gpio_suspend
- Return type: static int
- Signature: dwapb_gpio_suspend(struct device * dev)
- Line: 745
- Calls: dwapb_read, dwapb_write

### dwapb_irq_ack
- Return type: static void
- Signature: dwapb_irq_ack(struct irq_data * d)
- Line: 238
- Calls: dwapb_write, to_dwapb_gpio

### dwapb_irq_disable
- Return type: static void
- Signature: dwapb_irq_disable(struct irq_data * d)
- Line: 298
- Calls: dwapb_read, dwapb_write, to_dwapb_gpio

### dwapb_irq_enable
- Return type: static void
- Signature: dwapb_irq_enable(struct irq_data * d)
- Line: 282
- Calls: dwapb_read, dwapb_write, to_dwapb_gpio

### dwapb_irq_handler
- Return type: static void
- Signature: dwapb_irq_handler(struct irq_desc * desc)
- Line: 223
- Calls: dwapb_do_irq

### dwapb_irq_handler_mfd
- Return type: static irqreturn_t
- Signature: dwapb_irq_handler_mfd(int irq,void * dev_id)
- Line: 233
- Calls: dwapb_do_irq

### dwapb_irq_mask
- Return type: static void
- Signature: dwapb_irq_mask(struct irq_data * d)
- Line: 250
- Calls: dwapb_read, dwapb_write, gpiochip_disable_irq, to_dwapb_gpio

### dwapb_irq_set_type
- Return type: static int
- Signature: dwapb_irq_set_type(struct irq_data * d,u32 type)
- Line: 314
- Calls: dwapb_read, dwapb_toggle_trigger, dwapb_write, to_dwapb_gpio

### dwapb_irq_set_wake
- Return type: static int
- Signature: dwapb_irq_set_wake(struct irq_data * d,unsigned int enable)
- Line: 362
- Calls: to_dwapb_gpio

### dwapb_irq_unmask
- Return type: static void
- Signature: dwapb_irq_unmask(struct irq_data * d)
- Line: 266
- Calls: dwapb_read, dwapb_write, gpiochip_enable_irq, to_dwapb_gpio

### dwapb_offs_to_port
- Return type: static dwapb_gpio_port *
- Signature: dwapb_offs_to_port(struct dwapb_gpio * gpio,unsigned int offs)
- Line: 167
- Called by: dwapb_toggle_trigger

### dwapb_read
- Return type: static u32
- Signature: dwapb_read(struct dwapb_gpio * gpio,unsigned int offset)
- Line: 150
- Calls: gpio_reg_convert
- Called by: dwapb_do_irq, dwapb_gpio_set_debounce, dwapb_gpio_suspend, dwapb_irq_disable, dwapb_irq_enable, dwapb_irq_mask, dwapb_irq_set_type, dwapb_irq_unmask, dwapb_toggle_trigger

### dwapb_toggle_trigger
- Return type: static void
- Signature: dwapb_toggle_trigger(struct dwapb_gpio * gpio,unsigned int offs)
- Line: 181
- Calls: dwapb_offs_to_port, dwapb_read, dwapb_write
- Called by: dwapb_do_irq, dwapb_irq_set_type

### dwapb_write
- Return type: static void
- Signature: dwapb_write(struct dwapb_gpio * gpio,unsigned int offset,u32 val)
- Line: 158
- Calls: gpio_reg_convert
- Called by: dwapb_gpio_resume, dwapb_gpio_set_debounce, dwapb_gpio_suspend, dwapb_irq_ack, dwapb_irq_disable, dwapb_irq_enable, dwapb_irq_mask, dwapb_irq_set_type, dwapb_irq_unmask, dwapb_toggle_trigger

### gpio_reg_convert
- Return type: static u32
- Signature: gpio_reg_convert(struct dwapb_gpio * gpio,unsigned int offset)
- Line: 142
- Calls: gpio_reg_v2_convert
- Called by: dwapb_read, dwapb_write

### gpio_reg_v2_convert
- Return type: static u32
- Signature: gpio_reg_v2_convert(unsigned int offset)
- Line: 124
- Called by: gpio_reg_convert

### to_dwapb_gpio
- Return type: static dwapb_gpio *
- Signature: to_dwapb_gpio(struct gpio_chip * gc)
- Line: 108
- Called by: dwapb_irq_ack, dwapb_irq_disable, dwapb_irq_enable, dwapb_irq_mask, dwapb_irq_set_type, dwapb_irq_set_wake, dwapb_irq_unmask

## Structs (6)

### dwapb_context
- Line: 83
- Members:
  - fwnode: fwnode_handle *
  - idx: unsigned int
  - ngpio: unsigned int
  - gpio_base: unsigned int
  - irq: int[]
  - nports: unsigned int
  - data: u32
  - dir: u32
  - ext: u32
  - int_en: u32
  - int_mask: u32
  - int_type: u32
  - int_pol: u32
  - int_deb: u32
  - wake_en: u32
  - nr_irqs: unsigned int
  - irq: unsigned int[]
  - chip: gpio_generic_chip
  - pirq: dwapb_gpio_port_irqchip *
  - gpio: dwapb_gpio *
  - ctx: dwapb_context *
  - idx: unsigned int
  - dev: device *
  - regs: void __iomem *
  - nr_ports: unsigned int
  - flags: unsigned int
  - rst: reset_control *
  - clks: clk_bulk_data[]

### dwapb_gpio
- Line: 114
- Members:
  - fwnode: fwnode_handle *
  - idx: unsigned int
  - ngpio: unsigned int
  - gpio_base: unsigned int
  - irq: int[]
  - nports: unsigned int
  - data: u32
  - dir: u32
  - ext: u32
  - int_en: u32
  - int_mask: u32
  - int_type: u32
  - int_pol: u32
  - int_deb: u32
  - wake_en: u32
  - nr_irqs: unsigned int
  - irq: unsigned int[]
  - chip: gpio_generic_chip
  - pirq: dwapb_gpio_port_irqchip *
  - gpio: dwapb_gpio *
  - ctx: dwapb_context *
  - idx: unsigned int
  - dev: device *
  - regs: void __iomem *
  - nr_ports: unsigned int
  - flags: unsigned int
  - rst: reset_control *
  - clks: clk_bulk_data[]

### dwapb_gpio_port
- Line: 100
- Members:
  - fwnode: fwnode_handle *
  - idx: unsigned int
  - ngpio: unsigned int
  - gpio_base: unsigned int
  - irq: int[]
  - nports: unsigned int
  - data: u32
  - dir: u32
  - ext: u32
  - int_en: u32
  - int_mask: u32
  - int_type: u32
  - int_pol: u32
  - int_deb: u32
  - wake_en: u32
  - nr_irqs: unsigned int
  - irq: unsigned int[]
  - chip: gpio_generic_chip
  - pirq: dwapb_gpio_port_irqchip *
  - gpio: dwapb_gpio *
  - ctx: dwapb_context *
  - idx: unsigned int
  - dev: device *
  - regs: void __iomem *
  - nr_ports: unsigned int
  - flags: unsigned int
  - rst: reset_control *
  - clks: clk_bulk_data[]

### dwapb_gpio_port_irqchip
- Line: 95
- Members:
  - fwnode: fwnode_handle *
  - idx: unsigned int
  - ngpio: unsigned int
  - gpio_base: unsigned int
  - irq: int[]
  - nports: unsigned int
  - data: u32
  - dir: u32
  - ext: u32
  - int_en: u32
  - int_mask: u32
  - int_type: u32
  - int_pol: u32
  - int_deb: u32
  - wake_en: u32
  - nr_irqs: unsigned int
  - irq: unsigned int[]
  - chip: gpio_generic_chip
  - pirq: dwapb_gpio_port_irqchip *
  - gpio: dwapb_gpio *
  - ctx: dwapb_context *
  - idx: unsigned int
  - dev: device *
  - regs: void __iomem *
  - nr_ports: unsigned int
  - flags: unsigned int
  - rst: reset_control *
  - clks: clk_bulk_data[]

### dwapb_platform_data
- Line: 77
- Members:
  - fwnode: fwnode_handle *
  - idx: unsigned int
  - ngpio: unsigned int
  - gpio_base: unsigned int
  - irq: int[]
  - nports: unsigned int
  - data: u32
  - dir: u32
  - ext: u32
  - int_en: u32
  - int_mask: u32
  - int_type: u32
  - int_pol: u32
  - int_deb: u32
  - wake_en: u32
  - nr_irqs: unsigned int
  - irq: unsigned int[]
  - chip: gpio_generic_chip
  - pirq: dwapb_gpio_port_irqchip *
  - gpio: dwapb_gpio *
  - ctx: dwapb_context *
  - idx: unsigned int
  - dev: device *
  - regs: void __iomem *
  - nr_ports: unsigned int
  - flags: unsigned int
  - rst: reset_control *
  - clks: clk_bulk_data[]

### dwapb_port_property
- Line: 69
- Members:
  - fwnode: fwnode_handle *
  - idx: unsigned int
  - ngpio: unsigned int
  - gpio_base: unsigned int
  - irq: int[]
  - nports: unsigned int
  - data: u32
  - dir: u32
  - ext: u32
  - int_en: u32
  - int_mask: u32
  - int_type: u32
  - int_pol: u32
  - int_deb: u32
  - wake_en: u32
  - nr_irqs: unsigned int
  - irq: unsigned int[]
  - chip: gpio_generic_chip
  - pirq: dwapb_gpio_port_irqchip *
  - gpio: dwapb_gpio *
  - ctx: dwapb_context *
  - idx: unsigned int
  - dev: device *
  - regs: void __iomem *
  - nr_ports: unsigned int
  - flags: unsigned int
  - rst: reset_control *
  - clks: clk_bulk_data[]

## Variables (4)

- static **dwapb_acpi_match** : const struct acpi_device_id[] (line 692)
- static **dwapb_gpio_driver** : platform_driver (line 833)
- static **dwapb_irq_chip** : const struct irq_chip (line 377)
- static **dwapb_of_match** : const struct of_device_id[] (line 685)

## Macros (34)

- **DWAPB_DRIVER_NAME** (line 47)
- **DWAPB_MAX_GPIOS** (line 49)
- **DWAPB_MAX_PORTS** (line 48)
- **DWAPB_NR_CLOCKS** (line 65)
- **GPIO_EXT_PORTA** (line 42)
- **GPIO_EXT_PORTB** (line 43)
- **GPIO_EXT_PORTC** (line 44)
- **GPIO_EXT_PORTD** (line 45)
- **GPIO_EXT_PORT_STRIDE** (line 51)
- **GPIO_INTEN** (line 35)
- **GPIO_INTMASK** (line 36)
- **GPIO_INTMASK_V2** (line 59)
- **GPIO_INTSTATUS** (line 39)
- **GPIO_INTSTATUS_V2** (line 62)
- **GPIO_INTTYPE_LEVEL** (line 37)
- **GPIO_INTTYPE_LEVEL_V2** (line 60)
- **GPIO_INT_POLARITY** (line 38)
- **GPIO_INT_POLARITY_V2** (line 61)
- **GPIO_PORTA_DEBOUNCE** (line 40)
- **GPIO_PORTA_EOI** (line 41)
- **GPIO_PORTA_EOI_V2** (line 63)
- **GPIO_REG_OFFSET_MASK** (line 57)
- **GPIO_REG_OFFSET_V1** (line 55)
- **GPIO_REG_OFFSET_V2** (line 56)
- **GPIO_SWPORTA_DDR** (line 28)
- **GPIO_SWPORTA_DR** (line 27)
- **GPIO_SWPORTB_DDR** (line 30)
- **GPIO_SWPORTB_DR** (line 29)
- **GPIO_SWPORTC_DDR** (line 32)
- **GPIO_SWPORTC_DR** (line 31)
- **GPIO_SWPORTD_DDR** (line 34)
- **GPIO_SWPORTD_DR** (line 33)
- **GPIO_SWPORT_DDR_STRIDE** (line 53)
- **GPIO_SWPORT_DR_STRIDE** (line 52)
