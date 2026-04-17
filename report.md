# API Reliability Monitor — SLA Report

> Last updated: **2026-04-17 17:15 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.58% | 2006.8 | 10206.7 | 1000ms | 58/333 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 126.0 | 3806.8 | 1500ms | 1/333 |
| ❌ | `nasa_apod` | 65.77% | 43.54% | 3866.5 | 10538.0 | 2000ms | 188/333 |
| ❌ | `ipapi_check` | 92.79% | 100.0% | 160.4 | 353.0 | 2500ms | 0/333 |
| ⚠️ | `open_meteo_weather` | 97.6% | 96.4% | 788.7 | 14877.1 | 2000ms | 12/333 |
| ⚠️ | `dog_ceo_random` | 99.1% | 87.39% | 1002.8 | 10244.1 | 2500ms | 42/333 |
| ✅ | `useless_fact` | 99.4% | 99.1% | 587.4 | 10229.6 | 2500ms | 3/333 |
| ✅ | `catfact_random` | 99.4% | 99.7% | 252.4 | 10070.5 | 3000ms | 1/333 |
| ✅ | `agify_name` | 100.0% | 99.7% | 379.4 | 3237.1 | 2000ms | 1/333 |
| ✅ | `rest_countries` | 100.0% | 98.8% | 271.6 | 7269.1 | 2500ms | 4/333 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.7% | 239.8 | 2314.9 | 2000ms | 1/333 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.7 | 252.0 | 1500ms | 0/333 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 5840.5 | 88.89% |
| `nasa_apod` | 20:00 | 4815.7 | 68.18% |
| `nasa_apod` | 18:00 | 4765.6 | 76.92% |
| `nasa_apod` | 11:00 | 4698.9 | 61.9% |
| `nasa_apod` | 17:00 | 4582.4 | 63.16% |
| `numbers_trivia` | 00:00 | 4205.1 | 40.0% |
| `nasa_apod` | 10:00 | 4174.0 | 53.33% |
| `nasa_apod` | 21:00 | 4054.0 | 42.11% |
| `nasa_apod` | 14:00 | 4029.0 | 52.63% |
| `nasa_apod` | 05:00 | 3989.9 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
