# drivers/gpio/gpio-merrifield.c

Subsystem: drivers/gpio

## Functions (2)

### mrfld_gpio_get_pinctrl_dev_name
- Return type: static const char *
- Signature: mrfld_gpio_get_pinctrl_dev_name(struct tng_gpio * priv)
- Line: 52
- Called by: mrfld_gpio_probe

### mrfld_gpio_probe
- Return type: static int
- Signature: mrfld_gpio_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 69
- Calls: devm_tng_gpio_probe, mrfld_gpio_get_pinctrl_dev_name

## Variables (3)

- static **mrfld_gpio_driver** : pci_driver (line 135)
- static **mrfld_gpio_ids** : const struct pci_device_id[] (line 129)
- static **mrfld_gpio_ranges** : const struct tng_gpio_pinrange[] (line 23)

## Macros (1)

- **MRFLD_NGPIO** (line 21)
