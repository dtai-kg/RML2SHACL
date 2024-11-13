# RML2SHACL 

A tool to generate SHACL shapes from RML mapping files for RDF graphs validation. 


# Installation
- From PyPi package
```bash
pip install rml2shacl
```

- From source code:
```bash
python -m pip install poetry
poetry update
poetry build
```

# Usage

General usage info: 

```
usage: rml2shacl -i MAPPING_PATH [-o SHACL_PATH] [-logLevel LOGLEVEL] 

positional arguments:
  -i,--MAPPING_PATH <arg>           RML mapping path to be converted into SHACL shapes.

optional arguments:
  -o SHACL_PATH <arg>               SHACL output path 
  -h, --help                        show this help message and exit
  -l, --LOG_LEVEL <arg>             Logging level of this script. Possible values: INFO,DEBUG,WARN

```


To generate your shacl shapes: 

```bash 
python3 -m rml2shacl -i <path> [-o <path>]
```

Example:

```bash 
python3 -m rml2shacl -i mapping.rml.ttl -o ./output/
```

The generated SHACL shapes will be located in `./output/mapping-shape.ttl`



