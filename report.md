# API Reliability Monitor — SLA Report

> Last updated: **2026-04-09 05:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 305.6 | 588.9 | 1000ms | 0/165 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.1 | 234.1 | 1500ms | 0/165 |
| ❌ | `nasa_apod` | 81.21% | 73.33% | 1581.4 | 10538.0 | 2000ms | 44/165 |
| ❌ | `ipapi_check` | 92.73% | 100.0% | 154.4 | 252.2 | 2500ms | 0/165 |
| ⚠️ | `open_meteo_weather` | 95.15% | 95.76% | 948.9 | 14877.1 | 2000ms | 7/165 |
| ❌ | `dog_ceo_random` | 98.79% | 75.76% | 1565.0 | 5586.8 | 2500ms | 40/165 |
| ⚠️ | `useless_fact` | 98.79% | 99.39% | 605.7 | 10229.6 | 2500ms | 1/165 |
| ⚠️ | `catfact_random` | 98.79% | 99.39% | 292.0 | 10070.5 | 3000ms | 1/165 |
| ✅ | `agify_name` | 100.0% | 99.39% | 401.4 | 3237.1 | 2000ms | 1/165 |
| ✅ | `rest_countries` | 100.0% | 98.79% | 289.8 | 7269.1 | 2500ms | 2/165 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.39% | 247.4 | 2314.9 | 2000ms | 1/165 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 99.4 | 252.0 | 1500ms | 0/165 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 2978.7 | 45.45% |
| `open_meteo_weather` | 05:00 | 2968.6 | 16.67% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `nasa_apod` | 20:00 | 2672.7 | 36.36% |
| `dog_ceo_random` | 12:00 | 2515.8 | 40.0% |
| `nasa_apod` | 22:00 | 2502.9 | 27.27% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
