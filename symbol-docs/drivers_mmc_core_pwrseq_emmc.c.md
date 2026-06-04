# drivers/mmc/core/pwrseq_emmc.c

Subsystem: drivers/mmc

## Functions (4)

### mmc_pwrseq_emmc_probe
- Return type: static int
- Signature: mmc_pwrseq_emmc_probe(struct platform_device * pdev)
- Line: 59

### mmc_pwrseq_emmc_remove
- Return type: static void
- Signature: mmc_pwrseq_emmc_remove(struct platform_device * pdev)
- Line: 93

### mmc_pwrseq_emmc_reset
- Return type: static void
- Signature: mmc_pwrseq_emmc_reset(struct mmc_host * host)
- Line: 32

### mmc_pwrseq_emmc_reset_nb
- Return type: static int
- Signature: mmc_pwrseq_emmc_reset_nb(struct notifier_block * this,unsigned long mode,void * cmd)
- Line: 42

## Structs (1)

### mmc_pwrseq_emmc
- Line: 24
- Members:
  - pwrseq: mmc_pwrseq
  - reset_nb: notifier_block
  - reset_gpio: gpio_desc *

## Variables (3)

- static **mmc_pwrseq_emmc_driver** : platform_driver (line 108)
- static **mmc_pwrseq_emmc_of_match** : const struct of_device_id[] (line 101)
- static **mmc_pwrseq_emmc_ops** : const struct mmc_pwrseq_ops (line 55)

## Macros (1)

- **to_pwrseq_emmc**(p) (line 30)
