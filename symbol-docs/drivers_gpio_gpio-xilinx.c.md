# drivers/gpio/gpio-xilinx.c

Subsystem: drivers/gpio

## Functions (26)

### xgpio_dir_in
- Return type: static int
- Signature: xgpio_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 212
- Calls: gpiochip_get_data, xgpio_write_ch

### xgpio_dir_out
- Return type: static int
- Signature: xgpio_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 241
- Calls: gpiochip_get_data, xgpio_write_ch

### xgpio_exit
- Return type: static void __exit
- Signature: xgpio_exit(void)
- Line: 695

### xgpio_free
- Return type: static void
- Signature: xgpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 284

### xgpio_get
- Return type: static int
- Signature: xgpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 131
- Calls: gpiochip_get_data, xgpio_read_ch

### xgpio_init
- Return type: static int __init
- Signature: xgpio_init(void)
- Line: 688

### xgpio_irq_ack
- Return type: static void
- Signature: xgpio_irq_ack(struct irq_data * irq_data)
- Line: 326

### xgpio_irq_mask
- Return type: static void
- Signature: xgpio_irq_mask(struct irq_data * irq_data)
- Line: 371
- Calls: gpiochip_disable_irq

### xgpio_irq_unmask
- Return type: static void
- Signature: xgpio_irq_unmask(struct irq_data * irq_data)
- Line: 399
- Calls: gpiochip_enable_irq, xgpio_read_ch

### xgpio_irqhandler
- Return type: static void
- Signature: xgpio_irqhandler(struct irq_desc * desc)
- Line: 477
- Calls: xgpio_read_ch_all

### xgpio_probe
- Return type: static int
- Signature: xgpio_probe(struct platform_device * pdev)
- Line: 540
- Calls: xgpio_save_regs

### xgpio_read_ch
- Return type: static void
- Signature: xgpio_read_ch(struct xgpio_instance * chip,int reg,int bit,unsigned long * a)
- Line: 86
- Calls: xgpio_regoffset
- Called by: xgpio_get, xgpio_irq_unmask, xgpio_read_ch_all

### xgpio_read_ch_all
- Return type: static void
- Signature: xgpio_read_ch_all(struct xgpio_instance * chip,int reg,unsigned long * a)
- Line: 102
- Calls: xgpio_read_ch
- Called by: xgpio_irqhandler

### xgpio_regoffset
- Return type: static int
- Signature: xgpio_regoffset(struct xgpio_instance * chip,int ch)
- Line: 74
- Called by: xgpio_read_ch, xgpio_write_ch

### xgpio_remove
- Return type: static void
- Signature: xgpio_remove(struct platform_device * pdev)
- Line: 313

### xgpio_request
- Return type: static int
- Signature: xgpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 272

### xgpio_resume
- Return type: static int
- Signature: xgpio_resume(struct device * dev)
- Line: 330

### xgpio_runtime_resume
- Return type: static int
- Signature: xgpio_runtime_resume(struct device * dev)
- Line: 355

### xgpio_runtime_suspend
- Return type: static int
- Signature: xgpio_runtime_suspend(struct device * dev)
- Line: 346

### xgpio_save_regs
- Return type: static void
- Signature: xgpio_save_regs(struct xgpio_instance * chip)
- Line: 266
- Calls: xgpio_write_ch_all
- Called by: xgpio_probe

### xgpio_set
- Return type: static int
- Signature: xgpio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 151
- Calls: gpiochip_get_data, xgpio_write_ch

### xgpio_set_irq_type
- Return type: static int
- Signature: xgpio_set_irq_type(struct irq_data * irq_data,unsigned int type)
- Line: 440

### xgpio_set_multiple
- Return type: static int
- Signature: xgpio_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 178
- Calls: gpiochip_get_data, xgpio_write_ch_all

### xgpio_suspend
- Return type: static int
- Signature: xgpio_suspend(struct device * dev)
- Line: 289

### xgpio_write_ch
- Return type: static void
- Signature: xgpio_write_ch(struct xgpio_instance * chip,int reg,int bit,unsigned long * a)
- Line: 94
- Calls: xgpio_regoffset
- Called by: xgpio_dir_in, xgpio_dir_out, xgpio_set, xgpio_write_ch_all

### xgpio_write_ch_all
- Return type: static void
- Signature: xgpio_write_ch_all(struct xgpio_instance * chip,int reg,unsigned long * a)
- Line: 111
- Calls: xgpio_write_ch
- Called by: xgpio_save_regs, xgpio_set_multiple

## Structs (1)

### xgpio_instance
- Line: 59
- Members:
  - gc: gpio_chip
  - regs: void __iomem *
  - gpio_lock: raw_spinlock_t
  - irq: int
  - clk: clk *

## Variables (4)

- static **xgpio_dev_pm_ops** : const struct dev_pm_ops (line 362)
- static **xgpio_irq_chip** : const struct irq_chip (line 522)
- static **xgpio_of_match** : const struct of_device_id[] (line 671)
- static **xgpio_plat_driver** : platform_driver (line 678)

## Macros (12)

- **XGPIO_CHANNEL0_OFFSET** (line 27)
- **XGPIO_CHANNEL1_OFFSET** (line 28)
- **XGPIO_DATA_OFFSET** (line 24)
- **XGPIO_GIER_IE** (line 31)
- **XGPIO_GIER_OFFSET** (line 30)
- **XGPIO_IPIER_OFFSET** (line 33)
- **XGPIO_IPISR_OFFSET** (line 32)
- **XGPIO_TRI_OFFSET** (line 25)
- **xgpio_readreg**(offset) (line 37)
- **xgpio_readreg**(offset) (line 40)
- **xgpio_writereg**(offset,val) (line 38)
- **xgpio_writereg**(offset,val) (line 41)
