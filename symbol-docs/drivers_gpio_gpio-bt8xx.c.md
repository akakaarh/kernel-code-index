# drivers/gpio/gpio-bt8xx.c

Subsystem: drivers/gpio

## Functions (9)

### bt8xxgpio_gpio_direction_input
- Return type: static int
- Signature: bt8xxgpio_gpio_direction_input(struct gpio_chip * gpio,unsigned nr)
- Line: 68
- Calls: gpiochip_get_data

### bt8xxgpio_gpio_direction_output
- Return type: static int
- Signature: bt8xxgpio_gpio_direction_output(struct gpio_chip * gpio,unsigned nr,int val)
- Line: 98
- Calls: gpiochip_get_data

### bt8xxgpio_gpio_get
- Return type: static int
- Signature: bt8xxgpio_gpio_get(struct gpio_chip * gpio,unsigned nr)
- Line: 86
- Calls: gpiochip_get_data

### bt8xxgpio_gpio_set
- Return type: static int
- Signature: bt8xxgpio_gpio_set(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 120
- Calls: gpiochip_get_data

### bt8xxgpio_gpio_setup
- Return type: static void
- Signature: bt8xxgpio_gpio_setup(struct bt8xxgpio * bg)
- Line: 137
- Called by: bt8xxgpio_probe

### bt8xxgpio_probe
- Return type: static int
- Signature: bt8xxgpio_probe(struct pci_dev * dev,const struct pci_device_id * pci_id)
- Line: 153
- Calls: bt8xxgpio_gpio_setup

### bt8xxgpio_remove
- Return type: static void
- Signature: bt8xxgpio_remove(struct pci_dev * pdev)
- Line: 212
- Calls: gpiochip_remove

### bt8xxgpio_resume
- Return type: static int
- Signature: bt8xxgpio_resume(struct device * dev)
- Line: 243

### bt8xxgpio_suspend
- Return type: static int
- Signature: bt8xxgpio_suspend(struct device * dev)
- Line: 226

## Structs (1)

### bt8xxgpio
- Line: 48
- Members:
  - lock: spinlock_t
  - mmio: void __iomem *
  - pdev: pci_dev *
  - gpio: gpio_chip
  - saved_outen: u32
  - saved_data: u32

## Variables (3)

- static **bt8xxgpio_pci_driver** : pci_driver (line 271)
- static **bt8xxgpio_pci_tbl** : const struct pci_device_id[] (line 262)
- static **modparam_gpiobase** : int (line 63)

## Macros (3)

- **BT8XXGPIO_NR_GPIOS** (line 45)
- **bgread**(adr) (line 60)
- **bgwrite**(dat,adr) (line 59)
