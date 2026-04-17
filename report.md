# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 09:18 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 84.36% | 1833.1 | 10206.7 | 1000ms | 51/326 |
| ❌ | `public_apis_list` | 0.0% | 99.69% | 127.0 | 3806.8 | 1500ms | 1/326 |
| ❌ | `nasa_apod` | 65.34% | 43.56% | 3887.4 | 10538.0 | 2000ms | 184/326 |
| ❌ | `ipapi_check` | 93.25% | 100.0% | 160.0 | 353.0 | 2500ms | 0/326 |
| ⚠️ | `open_meteo_weather` | 97.55% | 96.32% | 794.8 | 14877.1 | 2000ms | 12/326 |
| ⚠️ | `dog_ceo_random` | 99.39% | 87.42% | 985.9 | 5586.8 | 2500ms | 41/326 |
| ✅ | `useless_fact` | 99.39% | 99.39% | 578.9 | 10229.6 | 2500ms | 2/326 |
| ✅ | `catfact_random` | 99.39% | 99.69% | 253.8 | 10070.5 | 3000ms | 1/326 |
| ✅ | `agify_name` | 100.0% | 99.69% | 381.4 | 3237.1 | 2000ms | 1/326 |
| ✅ | `rest_countries` | 100.0% | 98.77% | 274.4 | 7269.1 | 2500ms | 4/326 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.69% | 239.7 | 2314.9 | 2000ms | 1/326 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.5 | 252.0 | 1500ms | 0/326 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 17:00 | 4677.2 | 61.11% |
| `nasa_apod` | 10:00 | 4445.3 | 57.14% |
| `nasa_apod` | 11:00 | 4414.7 | 60.0% |
| `nasa_apod` | 14:00 | 4220.6 | 55.56% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
