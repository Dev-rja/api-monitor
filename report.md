# API Reliability Monitor — SLA Report

> Last updated: **2026-07-13 16:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.0% | 2099.4 | 10206.7 | 1000ms | 267/1405 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.3 | 4595.4 | 1500ms | 4/1405 |
| ❌ | `ipapi_check` | 74.8% | 99.93% | 154.0 | 4507.0 | 2500ms | 1/1405 |
| ❌ | `nasa_apod` | 75.3% | 51.03% | 3255.1 | 11152.5 | 2000ms | 688/1405 |
| ❌ | `dog_ceo_random` | 94.8% | 96.58% | 544.5 | 10244.1 | 2500ms | 48/1405 |
| ⚠️ | `open_meteo_weather` | 98.65% | 97.08% | 724.9 | 14877.1 | 2000ms | 41/1405 |
| ⚠️ | `rest_countries` | 98.93% | 98.65% | 311.2 | 10221.5 | 2500ms | 19/1405 |
| ✅ | `useless_fact` | 99.64% | 99.72% | 634.1 | 10229.6 | 2500ms | 4/1405 |
| ✅ | `catfact_random` | 99.79% | 99.36% | 256.1 | 10080.2 | 3000ms | 9/1405 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.6 | 4328.4 | 1500ms | 1/1405 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.4 | 16112.2 | 2000ms | 4/1405 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 209.1 | 3882.8 | 2000ms | 2/1405 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4055.0 | 54.79% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 01:00 | 3828.5 | 55.81% |
| `nasa_apod` | 18:00 | 3664.0 | 51.35% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 20:00 | 3476.5 | 50.56% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
