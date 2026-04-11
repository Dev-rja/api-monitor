# API Reliability Monitor — SLA Report

> Last updated: **2026-04-11 15:45 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **80.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 311.0 | 588.9 | 1000ms | 0/217 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.3 | 429.6 | 1500ms | 0/217 |
| ❌ | `nasa_apod` | 78.8% | 60.83% | 2260.1 | 10538.0 | 2000ms | 85/217 |
| ❌ | `ipapi_check` | 94.01% | 100.0% | 155.6 | 252.2 | 2500ms | 0/217 |
| ⚠️ | `open_meteo_weather` | 96.31% | 96.31% | 879.4 | 14877.1 | 2000ms | 8/217 |
| ⚠️ | `dog_ceo_random` | 99.08% | 81.11% | 1297.4 | 5586.8 | 2500ms | 41/217 |
| ✅ | `useless_fact` | 99.08% | 99.54% | 593.6 | 10229.6 | 2500ms | 1/217 |
| ✅ | `catfact_random` | 99.08% | 99.54% | 272.1 | 10070.5 | 3000ms | 1/217 |
| ✅ | `agify_name` | 100.0% | 99.54% | 402.5 | 3237.1 | 2000ms | 1/217 |
| ✅ | `rest_countries` | 100.0% | 98.62% | 295.5 | 7269.1 | 2500ms | 3/217 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.54% | 242.4 | 2314.9 | 2000ms | 1/217 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/217 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `nasa_apod` | 13:00 | 4268.1 | 66.67% |
| `nasa_apod` | 18:00 | 3228.9 | 62.5% |
| `nasa_apod` | 20:00 | 3176.1 | 50.0% |
| `nasa_apod` | 11:00 | 3069.2 | 53.33% |
| `useless_fact` | 03:00 | 2972.0 | 25.0% |
| `dog_ceo_random` | 13:00 | 2918.8 | 66.67% |
| `nasa_apod` | 22:00 | 2872.5 | 38.46% |
| `nasa_apod` | 15:00 | 2793.9 | 50.0% |
| `open_meteo_weather` | 05:00 | 2637.8 | 14.29% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
