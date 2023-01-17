# Changelog

All notable changes will be documented in this file

## [0.0.12](https://github.com/pablobascunana/youml-api/compare/af06caf...b106a91) (17-01-2023)

### Added
* [PR-98](https://github.com/pablobascunana/youml-api/pull/92) Create RabbitMQ producer
* [PR-86](https://github.com/pablobascunana/youml-api/pull/86) Add train endpoint
* [PR-85](https://github.com/pablobascunana/youml-api/pull/85) Encode and decode JWT
* [PR-71](https://github.com/pablobascunana/youml-api/pull/71) Retrieve training endpoint
* [PR-70](https://github.com/pablobascunana/youml-api/pull/70) Create training endpoint
* [PR-68](https://github.com/pablobascunana/youml-api/pull/68) Create new training model
* [PR-67](https://github.com/pablobascunana/youml-api/pull/67) Mark to train at dates in image and image label models
* [PR-66](https://github.com/pablobascunana/youml-api/pull/66) Training model

### Changed
* [PR-86](https://github.com/pablobascunana/youml-api/pull/86) Refactor mark-to-train endpoint
* [PR-85](https://github.com/pablobascunana/youml-api/pull/85) Bump tox version from 4.0.11 to 4.0.18
* [PR-84](https://github.com/pablobascunana/youml-api/pull/84) Rename some files references from youml-manager to youml-api
* [PR-69](https://github.com/pablobascunana/youml-api/pull/69) Bump tox version from 3.27.0 to 3.27.1
* [PR-72](https://github.com/pablobascunana/youml-api/pull/72) Rename repository from youml-manager to youml-api
* [PR-68](https://github.com/pablobascunana/youml-api/pull/68) Refactor migrations

## [0.0.11](https://github.com/pablobascunana/youml-api/compare/0953144...af06caf) (09-11-2022)

### Added
* [PR-60](https://github.com/pablobascunana/youml-api/pull/60) Add configuration for coverage in SonarCloud
* [PR-58](https://github.com/pablobascunana/youml-api/pull/58) Update changelog
* [PR-57](https://github.com/pablobascunana/youml-api/pull/57) Logout endpoint
* [PR-56](https://github.com/pablobascunana/youml-api/pull/56) Remove some required uuids in some models

### Changed
* [PR-59](https://github.com/pablobascunana/youml-api/pull/59) to_representation to get_created_at to return dates

### Fixed
* [PR-65](https://github.com/pablobascunana/youml-api/pull/65) Fix configuration for coverage in SonarCloud

### Removed
* [PR-62](https://github.com/pablobascunana/youml-api/pull/62) Remove CodeQL GitHub action

## [0.0.10](https://github.com/pablobascunana/youml-api/compare/2a747d6...0953144) (27-10-2022)

### Added
* [PR-54](https://github.com/pablobascunana/youml-api/pull/54) Delete images endpoint
* [PR-53](https://github.com/pablobascunana/youml-api/pull/53) Get images endpoint
* [PR-52](https://github.com/pablobascunana/youml-api/pull/52) Delete label endpoint
* [PR-50](https://github.com/pablobascunana/youml-api/pull/50) Create image-labels endpoint
* [PR-48](https://github.com/pablobascunana/youml-api/pull/48) Endpoint get labels

### Changed
* [PR-50](https://github.com/pablobascunana/youml-api/pull/50) Return image saved date in image endpoint


## [0.0.9](https://github.com/pablobascunana/youml-api/compare/2ed9f97...2a747d6) (23-10-2022)

### Added
* [PR-45](https://github.com/pablobascunana/youml-api/pull/45) Add storage_in field in project model and save it create project endpoint
* [PR-43](https://github.com/pablobascunana/youml-api/pull/43) Add file manager provider and local filesystem
* [PR-42](https://github.com/pablobascunana/youml-api/pull/42) Create image endpoint
* [PR-40](https://github.com/pablobascunana/youml-api/pull/40) ImageLabels model
* [PR-39](https://github.com/pablobascunana/youml-api/pull/39) Image model
* [PR-38](https://github.com/pablobascunana/youml-api/pull/38) Label model


## [0.0.8](https://github.com/pablobascunana/youml-api/compare/90712cb...2ed9f97) (18-10-2022)

### Added
* [PR-34](https://github.com/pablobascunana/youml-api/pull/34) Delete dataset and rename tests cases
* [PR-33](https://github.com/pablobascunana/youml-api/pull/33) Delete project

### Fixed
* [PR-35](https://github.com/pablobascunana/youml-api/pull/35) Remove SonarCloud and Codacy issues


## [0.0.7](https://github.com/pablobascunana/youml-api/compare/cd3a3b9...90712cb) (16-10-2022)

### Added
* [PR-30](https://github.com/pablobascunana/youml-api/pull/30) Get datasets endpoint
* [PR-31](https://github.com/pablobascunana/youml-api/pull/31) Create dataset endpoint
* [PR-32](https://github.com/pablobascunana/youml-api/pull/32) Dataset model


## [0.0.6](https://github.com/pablobascunana/youml-api/compare/34864f4...cd3a3b9) (15-10-2022)

### Added
* [PR-28](https://github.com/pablobascunana/youml-api/pull/28) Get projects endpoint
* [PR-27](https://github.com/pablobascunana/youml-api/pull/27) Create project endpoint
* [PR-25](https://github.com/pablobascunana/youml-api/pull/25) Project model


### Changed
* [PR-28](https://github.com/pablobascunana/youml-api/pull/28) Update createdDate to cratedAt fields in company and project tables
* [PR-24](https://github.com/pablobascunana/youml-api/pull/24) Change field CompanyId to company in user table


## [0.0.5](https://github.com/pablobascunana/youml-api/compare/fdf8a8d...34864f4) (13-10-2022)

### Added
* [PR-22](https://github.com/pablobascunana/youml-api/pull/22) Login endpoint
* [PR-21](https://github.com/pablobascunana/youml-api/pull/21) Login endpoint


## [0.0.4](https://github.com/pablobascunana/youml-api/compare/3b365b1...fdf8a8d) (10-10-2022)

### Added
* [PR-18](https://github.com/pablobascunana/youml-api/pull/18) Pytest coverage and HTML reports

### Changed
* [PR-17](https://github.com/pablobascunana/youml-api/pull/17) Move permissions to core package
* [PR-16](https://github.com/pablobascunana/youml-api/pull/16) Implement JWT to user verification
* [PR-15](https://github.com/pablobascunana/youml-api/pull/15) Rename user table and delete action field in company table

## [0.0.3](https://github.com/pablobascunana/youml-api/compare/fee5783...3b365b1) (10-10-2022)

### Added
* [PR-13](https://github.com/pablobascunana/youml-api/pull/13) User verification
* [PR-12](https://github.com/pablobascunana/youml-api/pull/12) Send email, verification email template, create and verify token
* [PR-8](https://github.com/pablobascunana/youml-api/pull/8) Update readme
* [PR-7](https://github.com/pablobascunana/youml-api/pull/7) Dependabot config

## [0.0.2](https://github.com/pablobascunana/youml-api/compare/d34ac30...fee5783) (01-10-2022)

### Added
* [PR-6](https://github.com/pablobascunana/youml-api/pull/6) Company view set and unit tests
* [PR-5](https://github.com/pablobascunana/youml-api/pull/5) Changelog
* [PR-2](https://github.com/pablobascunana/youml-api/pull/2) Company model and company foreign key in user model

## [0.0.1](https://github.com/pablobascunana/youml-api/compare/c607e63...d34ac30) (30-09-2022)

### Added
* [PR-3](https://github.com/pablobascunana/youml-api/pull/3) User model
* [PR-1](https://github.com/pablobascunana/youml-api/pull/1) Endpoint to create and get user by uuid. Unit tests

### Fixed
* [PR-4](https://github.com/pablobascunana/youml-api/pull/4) Hide secret key and other variables in .env files
