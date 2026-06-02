# drivers/spi/spi-pxa2xx-platform.c

Subsystem: drivers/spi

## Functions (9)

### pxa2xx_spi_exit
- Return type: static void __exit
- Signature: pxa2xx_spi_exit(void)
- Line: 219

### pxa2xx_spi_idma_filter
- Return type: static bool
- Signature: pxa2xx_spi_idma_filter(struct dma_chan * chan,void * param)
- Line: 16

### pxa2xx_spi_init
- Return type: static int __init
- Signature: pxa2xx_spi_init(void)
- Line: 213

### pxa2xx_spi_init_pdata
- Return type: static pxa2xx_spi_controller *
- Signature: pxa2xx_spi_init_pdata(struct platform_device * pdev)
- Line: 77

### pxa2xx_spi_init_ssp
- Return type: static int
- Signature: pxa2xx_spi_init_ssp(struct platform_device * pdev,struct ssp_device * ssp,enum pxa_ssp_type type)
- Line: 22

### pxa2xx_spi_platform_probe
- Return type: static int
- Signature: pxa2xx_spi_platform_probe(struct platform_device * pdev)
- Line: 141

### pxa2xx_spi_platform_remove
- Return type: static void
- Signature: pxa2xx_spi_platform_remove(struct platform_device * pdev)
- Line: 173

### pxa2xx_spi_ssp_release
- Return type: static void
- Signature: pxa2xx_spi_ssp_release(void * ssp)
- Line: 55

### pxa2xx_spi_ssp_request
- Return type: static ssp_device *
- Signature: pxa2xx_spi_ssp_request(struct platform_device * pdev)
- Line: 60

## Variables (3)

- static **driver** : platform_driver (line 202)
- static **pxa2xx_spi_acpi_match** : const struct acpi_device_id[] (line 185)
- static **pxa2xx_spi_of_match** : const struct of_device_id[] (line 196)
